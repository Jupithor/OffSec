#!/bin/bash

read -p 'username: ' username
read -p 'group: ' group

if id -nGz "$username" | grep -qzxF "$group"
then
        #both found and is member of group
        echo "Membership valid!"
elif getent passwd $username &>/dev/null  && getent group $group &>/dev/null
then
        #both found but is not member of group
        echo "Membership invalid but available to join."
elif getent passwd $username &>/dev/null  ||  getent group $group &>/dev/null
then
        #one is found
        echo "One exists, one does not. You figure out which."
else
        #both are not found
        echo "Both are not found - why are you even asking me this?"
fi
