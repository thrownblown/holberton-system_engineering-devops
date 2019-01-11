# Using Puppet, creates a file in /tmp

file { 'holberton':
  ensure  => 'file',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  path    => '/tmp/holberton',
  content => 'I love Puppet'
}
