#!/usr/bin/env perl
#Thank you Daniel Vinciguerra for collaborating with this code

use 5.10.0;
use strict;
use warnings;

use LWP::UserAgent;

# sites fonte
my $source_list = [
    'http://ipinfo.io/ip', 'http://checkip.dyndns.org'
];

my $ua = LWP::UserAgent->new;

for my $site (@$source_list){
    my $res = $ua->get($site);
    if($res->is_success){
        # parseando o ip
        $res->content =~ m/(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})/;
        open(my $res, '>', 'report.txt') or die;

        # tenta o proximo site caso não encontre
        next unless $1; 
        
        # retorna o ip
        say $1 and last;
    }
}
