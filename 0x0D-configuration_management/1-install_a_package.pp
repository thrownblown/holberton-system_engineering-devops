# Using Puppet, install puppet-lint.

package { 'puppet-lint':
  provider => 'gem',
  ensure   => '2.1.0'
}
