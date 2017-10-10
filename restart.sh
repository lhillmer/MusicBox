rm /etc/apache2/sites-available/MusicBox.conf
cp example.conf /etc/apache2/sites-available/MusicBox.conf
a2ensite MusicBox
systemctl restart apache2
systemctl restart mpd
