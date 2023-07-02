
$matchedVersion=Select-String -Path pyproject.toml "version = \x22(\d\.\d\.)(\d*)"  | Foreach-Object {$_.Matches}
$majorVersion = $matchedVersion.Groups[1].Value
$minorVersion = $matchedVersion.Groups[2].Value
$newVersion = $majorVersion+[string]([int]$minorVersion+1)
openapi-generator-cli generate -i openapi\jarviceAPI.json --git-repo-id python-jarviceapi --git-user-id nimbix  -g python-nextgen --additional-properties=packageName=jarviceapi_client,packageVersion=$newVersion