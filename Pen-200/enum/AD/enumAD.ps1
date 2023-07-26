#get domain object
$domainObj = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()

#Get primary DC name
$PDC = $domainObj.PdcRoleOwner.Name

#Get Distinguished Name(s)
$DN = ([adsi]'').distinguishedName

#LDAP format = LDAP://HostName[:PortNumber][/DistinguishedName] 
$LDAP = "LDAP://$PDC/$DN"

#Create new AD encapsulation
$direntry = New-Object System.DirectoryServices.DirectoryEntry($LDAP)

#Create new object to search the AD
$dirsearcher = New-Object System.DirectoryServices.DirectorySearcher($direntry)

#Filer for user accounts (samAccountType=805306368 (0x30000000))
$dirsearcher.filter="samAccountType=805306368"

#use findall method to return all entries within the filter (with root=$DN)
$result = $dirsearcher.FindAll()

#only print the properties of each user
Foreach($obj in $result)
{
    Foreach($prop in $obj.Properties)
    {
        $prop
    }

    Write-Host "-------------------------------"
}

