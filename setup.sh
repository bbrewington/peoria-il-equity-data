#############
# VARIABLES #
#############

# TODO: Change these variables to match your project
VENV_NAME=.venv;
PROJECT_DIR=peoria_dei_data; # Path relative to top-level git directory
REQ_TXT_RELATIVE_PATH=../requirements.txt; # Path relative to PROJECT_DIR

############
# OVERVIEW #
############

# This script will create a virtual environment for your project and install the packages listed in requirements.txt
# It works on both Windows and Unix-based systems (Linux, MacOS, etc.)

# Folder structure:
# - top-level git directory
#    - setup.sh
#    - requirements.txt <-- example...see comment on REQ_TXT_RELATIVE_PATH above 
#    - project_dir
#      - .venv

########
# CODE #
########

# Set working directory
cd $(git rev-parse --show-toplevel)/$PROJECT_DIR;

# Create .gitignore if doesn't exist
if [[ ! -e .gitignore ]]; then
    touch .gitignore;
fi

# Deactivate virtual environment if currently active
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo 'deactivating Virtual Env';
    deactivate;
fi

#   Set platform-specific subdir (handles if running this on Windows)
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    VENV_SUBDIR="Scripts";
    PYTHON_EXEC=python;
else
    VENV_SUBDIR="bin";
    PYTHON_EXEC=python3;
fi

# Make sure VENV_NAME is in .gitignore
if grep -q "^$VENV_NAME" .gitignore; then
    echo "Virtual environment already in .gitignore";
else
    echo $VENV_NAME >> .gitignore;
fi

# Create virtual environment & activate it
$PYTHON_EXEC -m venv $VENV_NAME;
source "$VENV_NAME/$VENV_SUBDIR/activate";
$PYTHON_EXEC -m pip install --upgrade pip;
pip install -r $REQ_TXT_RELATIVE_PATH;

# Add virtual environment to Jupyter Kernel
pip install ipykernel
$PYTHON_EXEC -m ipykernel install --user --name=$VENV_NAME
