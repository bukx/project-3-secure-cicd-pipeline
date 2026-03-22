path "secret/data/prod/database" { capabilities = ["read"] }
path "secret/data/prod/api"      { capabilities = ["read"] }
path "secret/data/prod/tls/*"    { capabilities = ["read"] }
path "secret/data/*"             { capabilities = ["deny"] }
path "auth/token/renew-self"     { capabilities = ["update"] }
path "auth/token/lookup-self"    { capabilities = ["read"] }
