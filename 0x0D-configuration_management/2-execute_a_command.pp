# Using Puppet, create a manifest that kills a process named killmenow.

exec { 'kill_process':
  provider => 'shell',
  command  => 'pkill killmenow'
}
