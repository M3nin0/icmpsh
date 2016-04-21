## Background

This code uses a big problem in ICMP, the creation of packages is up to the O.S , so it is easy to forge packets.
I am changing this code since I'm using it as a vital part of a work of my technician Computer Networks.
Thanks Nico and Bernardo. 

## Description

The code was changed for me that it functions in a completely invisible way for the User . Creating the possibility of Phishing testing with this program .


## Features

* Client/server architecture.
* The master can run either in Python code.
* The target system has to be Windows because the slave runs on that platform only for now.
* The user running the slave on the target system does not require administrative privileges.

## Usage

### Running the master

The master is straight forward to use. There are no extra libraries required for the C and Python versions. The Perl master however has the following dependencies:

* IO::Socket
* NetPacket::IP
* NetPacket::ICMP

When running the master, don't forget to disable ICMP replies by the OS. For example:
```
sysctl -w net.ipv4.icmp_echo_ignore_all=1
```

If you miss doing that, you will receive information from the slave, but the slave is unlikely to receive commands send from the master.

### Running the slave

To edit the following options directly access the source code.

```

Send a single test icmp request containing the string "Test1234" and then quit. 
                   This is for testing the connection.

Delay between requests in milliseconds 

Timeout of responses in milliseconds. If a response has not received in time, 
                   the slave will increase a counter of blanks. If that counter reaches a limit, the slave will quit.
                   The counter is set back to 0 if a response was received.

Limit of blanks (unanswered icmp requests before quitting

Maximal data buffer size in bytes
```


## License

This source code is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
