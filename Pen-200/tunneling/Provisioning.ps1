<# 
This script will create the flag_admin user and set the flag as the password.
WARNING: Do not run this in production using system account.
Last update: September 12, 2022
Last Updated By: Alice Admin
Duration: Unknown
Output: User created
#>

#Requires -RunAsAdministrator

$Flag="OS{b67e1e3fb24a386e006eb832842da139}";

$SecurePassword = $Flag | ConvertTo-SecureString -AsPlainText -Force

try {
    Write-Output "Searching for $Username in LocalUser DataBase"
    $UserAccount = Get-LocalUser $Username
    Write-Warning "$Username already exists, just going to reset password."
    $UserAccount | Set-LocalUser -Password $SecurePassword
} catch [Microsoft.PowerShell.Commands.UserNotFoundException] {
    Write-Output "$Username not found, creating the whole user."
    New-LocalUser $Username -Password $SecurePassword -FullName "FLAG USER" -Description "Flag User"
}

