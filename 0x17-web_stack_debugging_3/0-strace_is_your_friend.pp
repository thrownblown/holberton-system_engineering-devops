# fix settings file
exec { 'modify_file':
  command => "/bin/sed -i \'s/class-wp-locale.phpp/class-wp-locale.php/\' /var/www/html/wp-settings.php"
}
