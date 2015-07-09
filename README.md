# pwd.sh

Script to manage passwords in an encrypted file using gpg.

Passwords can be stored with and searched by a number of attributes, like platform, username, email, notes.

# Installation

    git clone https://github.com/tsiemens/pwds && cd pwds

Requires python and pip`

Install python-pip with your package manager, and install with sudo pip install gnupg

# Use

Run the script with `./pwds`

Use `./pwds [ command ] -h` for help.

`./pwds add [ options ]` to add a new password

`./pwds update [ options ]` to change a password

`./pwds show [ options ]` to view passwords. They can be searched by property.

The encrypted file pwds.safe`and script can be safely shared between machines over public channels (Google Drive, Dropbox, etc).
