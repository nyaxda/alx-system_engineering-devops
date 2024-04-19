# Using Puppet, install flask from pip3
package { 'python3-pip':
  ensure => installed,
}

# Using Puppet, install flask globally from pip3
exec { 'install-flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  require => Package['python3-pip'],
  path    => ['/bin', '/usr/bin'],
}
