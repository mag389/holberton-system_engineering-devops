# kills a process
exec {'killmenow':
  command => 'pkill killmenow',
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin']
}
