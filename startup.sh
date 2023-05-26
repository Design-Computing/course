#!/bin/sh
# https://stackoverflow.com/a/18425592/1835727
# alias python2='python'
# alias python='python3'
# https://stackoverflow.com/a/44377932/1835727
# alias pip2='pip'
# alias pip='pip3'

# echo 'export PATH="/Users/$USER/anaconda3/bin:$PATH"' >>.bash_profile

# This file installs a bunch of things that you'll find useful.
echo "Let's pip install a load of python libraries"
pip3 install -r requirements.txt
echo "And now we'll install a bunch of extensions for vs code"
code --install-extension Andreabbondanza.ignoregit
code --install-extension ban.spellright
code --install-extension dbaeumer.vscode-eslint
code --install-extension DotJoshJohnson.xml
code --install-extension esbenp.prettier-vscode
code --install-extension joelday.docthis
code --install-extension mechatroner.rainbow-csv
code --install-extension ms-mssql.mssql
code --install-extension ms-python.python
code --install-extension ms-vsliveshare.vsliveshare
code --install-extension redhat.vscode-yaml
code --install-extension travisthetechie.write-good-linter
code --install-extension Tyriar.sort-lines
code --install-extension Zignd.html-css-class-completion
code --install-extension oderwat.indent-rainbow
