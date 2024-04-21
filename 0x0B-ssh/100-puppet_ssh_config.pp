# Puppet code to configure SSH client

file_line { 'config for private key':
    path    => '/etc/ssh/ssh_config',
    line    => 'IdentityFile ~/.ssh/school',
    match   => '^IdentityFile',
}

file_line { 'refuse authentication':
    path    => '/etc/ssh/ssh_config',
    line    => 'PasswordAuthentication no',
    match   => '^PasswordAuthentication',
}
