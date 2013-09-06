#!/bin/bash

usage() {
	echo "Usage: $0 <username> <password>"
	exit 1
}

[[ $# -ne 2 ]] && usage;

HISTFILE=/dev/null
USERNAME=$1
PASSWORD=$2
CHPASSWD=`which chpasswd`
USERADD=`which useradd`

getent passwd $1 > /dev/null 2>&1
status=$?

[[ $status -gt 0 ]] && $USERADD -m -s /bin/bash $USERNAME && echo "User $USERNAME has been created"

echo "$USERNAME:$PASSWORD"  |$CHPASSWD && echo "The user $USERNAME has had their password set to $PASSWORD"
