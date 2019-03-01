# fix settings file
file { '/var/www/html/wp-settings.php'
  ensure => present,
}->
file_line { 'class-wp-locale.phpp'
  path => '/var/www/html/wp-settings.php',
  line => '/class-wp-locale.php',
  match => '/class-wp-locale.phpp',
}
