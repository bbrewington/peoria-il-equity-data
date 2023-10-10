import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
import os

def get_url_list():
    pass
    
def read_url_list(file_path):
    with open(file_path, 'r') as f:
        url_list = f.readlines()
    url_list = [x.strip() for x in url_list]
    return url_list

def process_url(url, use_local, local_page_dir=None):
    assert local_page_dir is not None, 'Must provide local_page_dir if use_local is True'
    assert os.path.isdir(local_page_dir), f'{local_page_dir} does not exist (need to manually create)'
    page_id = url.split('seq=')[-1]
    if use_local:
        print('Reading contents from local file')
        local_file = f'{local_page_dir}/{page_id}.html'
        with open(local_file, 'r') as f:
            print(f'  Reading: {local_file}')
            url_contents = f.read()
    else:
        print('Reading contents from web')
        try:
            url_contents = requests.get(url).text
        except:
            print(f'Error getting data for {url}')
        
        print(f'  Writing: ../data/scrape_run_20231009/pages/{page_id}.html')
        with open(f'../data/scrape_run_20231009/pages/{page_id}.html', 'w') as f:
            f.write(url_contents)

    return {'url_contents': url_contents, 'page_id': page_id}

def parse_business_information(fieldset_node):
    bus_info = re.sub('\n{2,}', '\n', fieldset_node.text)
    bus_info_list = [x for x in bus_info.split('\n') if x.find(':') > 0]
    bus_info_dict = {}
    for item in bus_info_list:
        key = item[:item.find(': ')]
        value = item[item.find(': ')+2:]
        bus_info_dict[key] = value
    return bus_info_dict

def get_html_table_rows(page_content):
    soup = BeautifulSoup(page_content, "html.parser")
    table = soup.find(name='table', attrs={'class': 'sftable'})
    
    for br in table.find_all("br"):
        br.replace_with("\n" + br.text) # note, </br> tags can technically contain text

    rows = table.findAll(lambda tag: tag.name=='tr')
    
    return rows

def parse_table(rows):
    return_dict = {}

    for row in rows:
        fieldset_node = row.find('td').find('fieldset')
        legend_text = fieldset_node.find('legend').text
        
        if legend_text == 'Business Information':
            return_dict['business_information_raw'] = fieldset_node.text
            return_dict['business_information'] = parse_business_information(fieldset_node)
            return_dict['business_information_addl'] = fieldset_node.text[len(legend_text):]
            ownership_text_match = re.search('This is an? (.+)-Owned Business', fieldset_node.text)
            ownership_text = ownership_text_match.group(1) if ownership_text_match is not None else ''
            return_dict['Ownership Text'] = ownership_text
            return_dict['Owner African American'] = ownership_text.find('African American') >= 0
            return_dict['Owner Hispanic'] = ownership_text.find('Hispanic') >= 0
            return_dict['Owner Asian'] = ownership_text.find('Asian') >= 0
            return_dict['Owner Veteran'] = ownership_text.find('Veteran') >= 0
            return_dict['Owner Female'] = ownership_text.find('Female') >= 0
        else:
            return_dict[legend_text] = fieldset_node.text[len(legend_text):]

    return_dict_flattened = {}
    for k,v in return_dict.items():
        if type(v) == dict:
            for k2,v2 in v.items():
                return_dict_flattened[k2] = v2
        else:
            return_dict_flattened[k] = v
    
    return return_dict_flattened

def run_scrape(url_list_file_path, pages_dir_path, use_local):
    result_df_list = []
    url_list = read_url_list(url_list_file_path)
    for url in url_list:
        processed_url = process_url(url=url, local_page_dir=pages_dir_path, use_local=use_local)
        page_content = processed_url['url_contents']
        rows = get_html_table_rows(page_content)
        return_dict_flattened = parse_table(rows)
        return_dict_flattened['page_id'] = processed_url['page_id']
        return_dict_flattened['url'] = url
        result_df_list.append(pd.DataFrame(return_dict_flattened, index=[0]))

    df = pd.concat(result_df_list)
    
    return df

if __name__ == '__main__':
    df = run_scrape(
        url_list_file_path='../data/scrape_run_20231009/business_pages.txt',
        pages_dir_path='../data/scrape_run_20231009/pages',
        use_local=False)
    
    output_csv_file_path = '../data/scrape_run_20231009/business_pages_parsed.csv'
    print(f'Saving to {output_csv_file_path}')
    df.to_csv(output_csv_file_path, index=False)
