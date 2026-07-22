System design study guide 

- general

	- the software development life cycle (SDLC) has 6 phases: requirements gathering, design, implementation, testing, deployment, maintenance

	- dependency injection: an object or function receives other objects/functions it requires instead of creating them internally to maintain thread-safety

	- OS process management

		- the RR scheduling algorithm schedules processes with equal priority, allocating time slices to each process that it can run for so all processes get a fair share of CPU time

		- interrupts are signals sent to processes to indicate an event has occurred, signals sent to the CPU by hardware/software, telling the CPU to stop processing and start processing some other task, events such as a keyboard or mouse event or a timer running out which can cause interrupt signals to be sent, where the CPU saves the current process state and starts running the interrupt handler

		- swapping is done so data can be accessed easier, including process swapping which allows moving inactive processes from main memory to disk memory to free up space in main memory, where memory swapping allows moving blocks of memory from main memory to disk memory

		- cycle stealing uses extra unused clock cycles of another task to perform unrelated tasks

	- OOPS principles
		- Inheritance: 
			- allows reusing code across classes by sharing attributes and methods between parent/base and child/derived classes, can be hierarchical, hybrid, single, multiple, or multilevel inheritance in python
		- Abstraction: 
			- allows defining interfaces to determine how a class is implemented without implementing it in the abstract class or interface
		- Encapsulation: bundles data/attributes and methods/functions in a single unit like a class, and restricts direct access to some of the components to protect data integrity and ensure control over how its accessed/modified
			- internal details of a class are hidden, access modifiers (public, protected, private) control visibility of class attributes and methods, and getter/setter methods allow controlled access to private attributes
			- public attributes/methods are accessible from anywhere, protected attributes/methods are prefixed with an underscore and are intended to only be accessed within a class/subclasses, private attributes/methods are prefixed with double underscores and not directly accessible outside the class but can be accessed with name mangling
			- encapsulation allows data security by preventing unauthorized access/modification, code maintainability, and flexibility allowing changes to internal implementation without affecting external code
		- Polymorphism: the ability of a function/method/operator to behave differently based on the object its working with, allowing for flexibility and reusability in code and making it easy to work with objects of different types in the same way
			- method polymorphism is where different classes have methods with the same name with different functionality
			- operator polymorphism is where operators like  can perform different operations based on data types, either adding integers or concatenating strings
			- function polymorphism is where functions can handle arguments of different types like adding integers or concatenating strings
			- polymorphism with inheritance is where a child class overrides a method from its parent class, providing its own implementation
			- polymorphism is useful for code reusability, flexibility by extending functionality through adding new classes/methods, and readability
			- operator overloading allows existing operators to be redefined so they can be used for different purposes

	- digital signature: encrypted message digest (message digest can be the hash of the message to create a unique identifier of the data to detect changes in data)

	- data buffer: physical memory (often RAM) that temporarily stores data while being moved between different locations, which help synchronize data flow so components operating at different speeds can work together
		- buffers optimize performance by reducing the number of I/O operations which are usually slower than in-memory operations
		- buffers are used to read/write large files efficiently
		- networking data is buffered during transmission to optimize performance
		- buffers allow slicing/manipulation of large datasets without copying
		- the buffer protocol allows objects to expose underlying memory to other objects which is useful for zero-copy operations where data is shared without creating copies
		- objects like bytes/bytearray/memoryview implement buffers
		- buffers are useful to get more than one view on the data without holding multiple copies in memory
		- flush transfers data from the program buffer to the OS buffer or directly to file/disk, allows writing immediately as opposed to waiting for the automatic flusher to flush when the buffer is full or when the file is closed
	
	- pointer: a pointer is a variable that stores the address of a value in memory

	- recursion
		- recursion is where a function calls itself to solve a problem by breaking it into smaller subproblems, such as calculations, tree traversals or divide-and-conquer algorithms
			def recursive(param):
				if base_case:
					return base_param_result # prevents infinite recursion with a stopping case
				if recursive_case:
					return recursive(modified_params)
		- tail recursion is where the recursive call is the last thing the function does so no more code is executed after it returns, which is sometimes implemented like a loop to save memory, like where multiplication happens in a parameter definition so the multiplication happens before the recursive call
		- non-tail recursion is where the function does more work after the recursive call returns so it cant be optimized into a loop, like where there is multiplication after the recursive call by being outside the function call
		- recursion is easier to implement when the problem is recursive like tree traversals
		- iteration involves loops (for/while) to repeat a block of code which is usually more memory efficient than recursion, bc it doesnt involve multiple stack frames like recursion
		- avoid recursion when the problem can be easily solved with loops, when recursion depth is large which risks a stack overflow, when performance is critical and function call overhead matters
		- recursion is useful for simplicity and reduced code length, but increases memory overhead especially for deep recursion and has more function calls/returns so may have slower responses and risks stack overflow if the recursion depth exceeds the stack limit

	- stack overflow: occurs when the stack like a call stack (memory used to store active function calls) is full and an attempt to push an element on to it is made, which happens bc the stack has a fixed size or memory limit, which is a common issue in recursive functions where excessive function calls consume the call stack memory like with infinite recursion

	- SOLID concepts
		- Single Responsibility: a class should only have one responsibility
		- Open-Closed: entities should be open for extension but closed for modification (add functionality without changing the existing code)
		- Liskov Substitution: objects of a parent superclass should be replaceable with objects of its child subclasses without changing program correctness
		- Interface Segregation: clients shouldnt depend on interfaces they dont use, suggesting splitting larger interfaces into smaller interfaces
		- Dependency Inversion: high-level modules shouldnt depend on low-level modules as both should depend on abstractions, and abstractions shouldnt depend on details, details should depend on abstractions
	
	- how to optimize sql queries
		- limit results, select specific fields, use indexes, identify bottlenecks in execution plans using EXPLAIN or EXPLAIN PLAN, avoid correlated subqueries and replace with joins/temporary tables
	
	- thread-safe:
		- functions correctly when accessed by multiple threads concurrently. In a multi-threaded environment, thread-safe code prevents unexpected behavior, race conditions, or data corruption
		- race conditions: when multiple threads access/modify shared data at once, leading to inconsistent results
		- fix: 
			- avoid shared state completely by re-entrancy (code can be safely interrupted and resumed as threads have their own local state)
			- share immutable objects whose state cant be changed after creation so only read-only data is shared
			- synchronization mechanisms can be used when state has to be shared, mechanisms like:
				- mutual exclusion (ensuring only one thread accesses data at a time using locks or mutexes)
				- atomic operations (using operations that are indivisible ensuring that shared data is consistent)
				- though synchronization can lead to deadlocks and negatively impact performance bc it requires acquiring/releasing locks
			- A deadlock occurs in multithreaded applications when two or more threads are waiting for each other to release resources, causing all of them to be stuck indefinitely
			- to prevent deadlocks, use mutual exclusion, resource holding, and circular waits


- OS
	- Disk (Physical Storage Device)
		- A disk is a physical hardware device used to store data persistently, a disk doesn’t understand files or directories — only blocks of binary data.
		- examples: Hard Disk Drive (HDD), Solid-State Drive (SSD), NVMe Drive, USB Flash Drive
			/dev/sda → first SATA/SCSI disk
			/dev/nvme0n1 → first NVMe drive
			/dev/mmcblk0 → eMMC (embedded flash)
	- Device
		- In Linux, a device is an abstraction provided by the kernel representing a physical or virtual hardware component.
		- Every device (like a disk, keyboard, or network card) is represented as a file in /dev.
		- Disk devices = block devices (because they read/write blocks of data).
		- examples: 
			lsblk
				# NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
				# sda      8:0    0  100G  0 disk
				# ├─sda1   8:1    0   96G  0 part /
				# └─sda2   8:2    0    4G  0 part [SWAP]
	- Block
		- A block is the smallest unit of data transfer between the OS and a block device (usually 512 bytes or 4 KB); if the disk is a book, each block is a page.
		- The OS reads/writes entire blocks, not individual bytes.
		- Blocks are identified by a block number (offset) and are managed by the block layer of the kernel.
			sudo blockdev getbsz /dev/sda
		    	# -> 4096
	- Partition
		- A partition divides a single physical disk into multiple logical sections, where each section behaves like a separate disk.
		- Partitions allow multiple operating systems or filesystems on one disk.
		- examples:
			/dev/sda1 → root filesystem (/)
			/dev/sda2 → swap area
			/dev/sda3 → home partition
		- tools: fdisk, parted, lsblk
			sudo fdisk -l /dev/sda
	- Filesystem
		- A filesystem defines how files and directories are organized and stored within a partition, adding structure and metadata on top of raw blocks.
		- examples: ext4, xfs, btrfs, ntfs, fat32.
		- a filesystem maps files to blocks on disk, tracks free/used space, does journaling (for crash recovery), handles permissions and metadata
		- examples:
			sudo mkfs.ext4 /dev/sda1   # Create filesystem
			sudo fsck /dev/sda1        # Check/repair filesystem
	- Volume
		- A volume is a logical abstraction of storage space that may span multiple disks or partitions.
		- volume types:
			- Simple volume: one partition = one volume
			- Logical volume (LVM): can span multiple disks
			- RAID volume: combines multiple disks for redundancy/performance
		- volumes are managed by:
			- LVM (Logical Volume Manager): /dev/mapper/vgname-lvname
			- mdadm for RAID
		- examples:
			sudo lvs
				# LV   VG   Attr       LSize  Pool Origin Data%
				# root vg0  -wi-ao-  50.00g
	- Mount
		- Mounting attaches a filesystem to the Linux directory tree, making its files accessible.
		- Linux has a single unified directory hierarchy starting at /.
		- You can mount disks or partitions anywhere (e.g., /mnt/data, /home, /boot).
		- examples:
			sudo mount /dev/sda1 /mnt
			df -hT
				# Filesystem     Type  Size  Used Avail Mounted on
				# /dev/sda1      ext4   50G   10G   40G /mnt
		- To persist mounts: edit /etc/fstab.
	- Kernel
		- The kernel is the core of the operating system that manages all hardware interactions — including disks, memory, CPUs, and I/O.
		- the kernel manages storage components like device drivers (for disks, SSDs, RAID, etc.), provides the block device layer, implements VFS (Virtual File System) to unify filesystems, and handles syscalls like read(), write()
		- The kernel is the “traffic controller” between user programs and hardware.
		- examples:
			- Shows the running kernel version
				uname -r

	- User Space (Applications, Shell, File I/O commands, e.g. cp, cat, ls, vim, docker)
		- System Calls
			- Kernel (Device Drivers, Block Layer, Virtual File System (VFS))
				- Filesystem (ext4, xfs, btrfs, etc.): Organizes files/directories over raw blocks
					- Partition (/dev/sda1): Defined in partition table (MBR/GPT format)
						- Disk Device (/dev/sda, /dev/nvme0n1): Physical hardware       
							- Physical Media (HDD, SSD, NVMe, RAID)  

		- A user program writes a file, the filesystem decides which blocks on a partition to store it, the kernel’s block device driver translates that into hardware commands, the disk stores those bytes on the physical media.

- networks

	- Diagnostic & Monitoring Concepts
		- Traceroute								Shows the path packets take through routers.																	traceroute 8.8.8.8
		- Ping										Tests reachability and latency between hosts.																	ping -c 4 example.com
		- Netstat / ss								Shows open sockets and listening services.																		ss -tulnp
		- Tcpdump / Wireshark						Captures and analyzes network packets.																			sudo tcpdump -i eth0
		- Ifconfig / ip								Configures network interfaces.																					ip addr, ip route
		- MTR										Combines ping and traceroute for continuous network analysis.													mtr 8.8.8.8
		
	- Hardware & Link Layer Concepts
		- NIC (Network Interface Card)				Physical (or virtual) hardware that connects a computer to a network. Each NIC has its own MAC address.			lspci
		- MAC Address (Media Access Control)		A unique 48-bit identifier for a NIC. Used for communication within the same local network (Layer 2).			Example: 00:1A:2B:3C:4D:5E
		- Duplex									How data flows on a connection: Half: data flows 1-way at a time, Full: simultaneous send/receive				Check with: ethtool eth0
		- Bandwidth									Maximum data transfer rate of a connection (e.g., 1 Gbps).														Measure with iperf3
		- MTU (Maximum Transmission Unit)			Largest packet size (in bytes) that can be transmitted without fragmentation. Default: 1500 bytes for Ethernet.	View: ip link show eth0, Change: ip link set eth0 mtu 1400
		- ARP (Address Resolution Protocol)			Maps IP addresses to MAC addresses on a local network. Used when sending packets within a LAN.					arp -n or ip neigh show
		- Link / Layer 2							The local segment that connects devices using MAC addresses.													E.g., Ethernet, Wi-Fi, Switches
		
	- Network Layer Concepts
		- IP (Internet Protocol)					Handles addressing and routing of packets between networks. Each device gets an IP (IPv4 or IPv6).				ip addr show
		- IPv4 Address								32-bit address like 192.168.1.10. Divided into network and host portions.										CIDR: 192.168.1.0/24
		- Subnet									Logical division of an IP network; defines which IPs belong to the same local network.							192.168.1.0/24 → 256 addresses
		- Subnet Mask								Determines the size of the subnet; defines which IPs are local													255.255.255.0 = /24 = 256 IPs.	Convert: /24 → 255.255.255.0
		- Gateway									Router address used to send packets outside the local subnet.													Example: Default route 192.168.1.1
		- Route / Routing Table						Decides where packets go next (local, gateway, or drop).														ip route show
		- NAT (Network Address Translation)			Translates private IPs (like 192.168.x.x) to a single public IP for Internet access.							iptables -t nat -L -n -v
		- Firewall									Filters network traffic based on rules. Can allow, block, or modify packets.									iptables, ufw, firewalld
		- QoS (Quality of Service)					Prioritizes certain traffic types to ensure stable performance (e.g., VoIP > downloads).						Implemented via tc (traffic control)
		- Packet									Basic unit of network data — contains headers (IP/TCP) and payload.												View with: tcpdump -i eth0 -n
		
	- Transport Layer Concepts
		- Port										Virtual communication endpoint (0–65535). Identifies services (e.g., 80 = HTTP, 22 = SSH).						Check: ss -tulnp
		- TCP (Transmission Control Protocol)		Reliable, connection-oriented protocol ensuring ordered delivery and retransmission. Used by HTTP, SSH, etc.	States: SYN, ACK, FIN, etc.
		- UDP (User Datagram Protocol)				Fast, connectionless protocol — no delivery guarantees. Used by DNS, video streaming, VoIP.						DNS = UDP 53
		- Socket									Combination of IP and Port used by processes to communicate.													Example: 192.168.1.10:80
		- SYN / ACK / FIN							TCP flags used in connection setup and teardown: 																View with `tcpdump -i eth0 'tcp[tcpflags] & (tcp-syn
														- SYN: synchronize (start handshake)
														- ACK: acknowledge
														- FIN: finish connection	
														- TCP 3-Way Handshake:
															- 1. Client to Server: SYN
															- 2. Server to Client: SYN-ACK
															- 3. Client to Server: ACK (Connection established)

	- Session Layer Concepts
		- manages communication sessions — meaning how two systems establish, maintain, synchronize, and close long-running connections.
		- Session establishment, maintenance, and termination: handles when a session starts and ends (HTTP cookies, web sessions, or database connection pooling)
		- Dialog control: determines whether communication is half-duplex (one-way at a time) or full-duplex (two-way simultaneously) (RPC (Remote Procedure Calls), WebSockets, SSH sessions)
		- Synchronization points / checkpoints: allows recovery if a session fails — like saving state in a long data transfer (SMB file transfers, streaming protocols (RTSP))
		- Session recovery / re-establishment: restarting communication without redoing the entire process.
		- State management: applications using OAuth sessions, VPN tunnels, etc
		- session layer protocols
			- RPC (Remote Procedure Call)                 Manages client–server calls and returns
			- NetBIOS                                     Handles session setup between Windows hosts
			- PPTP (Point-to-Point Tunneling Protocol)    Manages VPN session control
			- SQL Session Layer                           Manages persistent connections between clients and databases
			- SOCKS                                       Session-based proxy protocol for network communication
			- SIP (Session Initiation Protocol)           Sets up and tears down voice/video sessions (VoIP)
		- The session layer (TLS handshake) establishes encryption keys and session state.
			- When you open an SSH connection, the transport layer (TCP) opens a reliable channel.
			- The session layer logic (within SSH) negotiates authentication, encryption, and keeps the session state alive.
			- If the network drops, SSH may resume from its last state

	- Presentation Layer Concepts
		- The presentation layer encrypts and decrypts HTTP messages, and deals with how data is represented, encoded, and transformed so that the receiver can understand it — even if the sender uses a different data format.
		- Data encoding										JSON, XML, YAML, Protobuf, ASN.1
		- Compression										gzip, Brotli, zlib
		- Encryption										TLS/SSL, SSH, AES, RSA
		- Serialization										Python’s pickle, Java serialization, Google Protocol Buffers
		- Character encoding								UTF-8, UTF-16, ASCII
		- protocols
			- TLS/SSL										Encrypts and authenticates data between hosts
			- MIME (Multipurpose Internet Mail Extensions)	Defines file type and encoding for email/web
			- ASN.1 (Abstract Syntax Notation One)			Defines structured data representation (used in SNMP, X.509)
			- XDR (External Data Representation)			Encodes data in RPC calls
			- JSON / XML / YAML								Human-readable serialization formats
			- Protobuf / Avro / Thrift						Efficient binary serialization

	- Application Layer Concepts
		- The application layer (HTTP) reads or writes the actual web content (HTML, JSON, etc.).
		- DNS: Domain Name System					Translates domain names to IP addresses.																		dig example.com, nslookup
		- DHCP: Dynamic Host Configuration Protocol	Automatically assigns IPs, subnet masks, and gateways to clients.												View leases: cat /var/lib/dhcp/dhclient.leases
		- VPN: Virtual Private Network				Encrypts traffic and routes it through a secure tunnel. 														Common protocols: OpenVPN, WireGuard, IPSec.	Check tunnel: `ip a
		- Proxy Server								Intermediary that forwards requests and can cache, filter, or hide client identity.								export http_proxy=http://proxy:8080
		- HTTP / HTTPS								Application protocols that run on TCP (ports 80/443).															Test with curl -v https://example.com
		
	- For a client accessing https://example.com:
		- DNS resolves example.com to 93.184.216.34
		- Browser opens socket to 93.184.216.34:443
		- TCP handshake: SYN then SYN-ACK then ACK
		- TLS (encryption) starts (for HTTPS)
		- Packets travel through NIC, subnet, gateway, and possibly NAT
		- The firewall and QoS may filter or prioritize packets
		- Data arrives on the server’s port 443, which is handled by the kernel and passed to the web server process
		- Responses are sent back, acknowledged by TCP
					
	- OSI protocol communication steps
			7		Application		Browser requests a web page (DNS, HTTP, HTTPS, SSH, SMTP)
			6		Presentation	Data encrypted with TLS (TLS/SSL, SSH, AES, RSA, JSON, XML, ASN.1 (used in SNMP, X.509), XDR (encodes data in RPC calls), MIME, gzip, YAML, zlib, UTF-8, UTF-16, ASCII - Data formatting, encoding, serialization, syntax negotiation, translation, encryption, compression)
			5		Session			TLS session established and maintained (RPC, SIP, SSH, SOCKS, PPTP, SMB - Connection control, synchronization/coordination, session/dialog management, recovery)
			4		Transport		TCP connection ensures reliable delivery (TCP, UDP)
			3		Network			IP routes packets to destination (IP, Subnet, Gateway, NAT, Routing)
			2		Link/Data Link	Ethernet frames sent on LAN (ARP, MAC, Ethernet, MTU, QoS, Duplex, framing, error detection)
			1		Physical		Bits transmitted over cable or Wi-Fi (NIC, signaling, wires/cables, radio signals, wi-fi)
		
	- subnet mask: tells computer which part of the IP address is the network and which is the host part, to determine if an IP address is on the same network as the computer requesting the info; if the requesting computer and the requested computer have the same subnet mask, they can assume theyre on the same network
		- subnetting divides a network into smaller subnets, each with its own IP address and subnet mask, which allows controlling traffic flow and conserving IP addresses and segmenting networks into different security zones

	- network address translation (NAT) tells the computer's network card how to communicate with other computers on the internet by translating IP addresses, allowing multiple devices on a network to use the same IP address, modifying the IP packet headers as they go through a router or firewall

	- tunnel mode: tunnel mode allows for efficient network usage by breaking data into smaller packets and sending them through a tunnel

	- ethernet: a tech standard for local area networks, connecting computers in a limited geographical area using special cables and operating a higher speed than other LAN technologies, using a bus or star topology

	- network models

		- IPSEC
			- an Internet Protocol network's communications can be secured using IPSEC
				- Authenticating Header: authenticates the sender/recipient of data
				- Encapsulating Security Payload: encrypts data 
			- IPSEC offers data integrity (ensuring data hasnt been changed), data origin authentication, encryption (no one can read data except authorized receivers), replay protection, and network-level peer authentication
			- supports transport and tunnel modes

		- internet protocol suite (TCP/IP)
			- link layer: includes protocols relevant to a local network (a link or IP network), where the computers are physically wired on the same network so they dont need a router and MAC addresses to communicate
			- internet layer: includes protocols relevant to connecting different IP networks like IPv6
			- transport layer: includes protocols for direct communication channels over the internet like TCP
			- application layer: includes protocols relevant to applications sending data to and from users over the internet like HTTP

		- open systems interconnection model (OSI)
			- physical layer: transmits raw data on hardware like Ethernet
			- data link layer: establishes connections for data transfer between computers in the same physical network like with MAC addresses
			- network layer: establishes connections for data transfer in packets between computers in different networks, like IP networks
			- transport layer: transfers data with reliable quality like TCP
			- session layer: manages data transfer sessions between computers
			- presentation layer: translates lower layer data formats for use by the application layer
			- application layer: application-enabling functionality like HTTP

	- protocols and how they fit into network models
		- IP (internet protocol)
			- allows computers on different physical networks to communicate
			- is in the internet layer of TCP/IP and the network layer of OSI
			- defines and works with the packet, the fundamental data unit, and provides addressing as IP addresses so packets can be correctly routed
			- an IP packet consists of headers and data, the header contains info like the source/destination address, the data is formatted and contains whatever is useful for the next layeres
		- TCP (transport control protocol)
			- manages reliability of data transferred with IP
			- corresponds to the transport layer in TCP/IP and the transport layer of OSI
			- establishes connections between client and server and then transfers data
			- TCP builds on IP to add guarantees that data messages are delivered reliably, in order, and checked for errors
			- if the application needs faster data transfer and doesnt need confirmed connections it can use the similar User Datagram Protocol (UDP) instead, which works at the same layer as TCP but without guarantees about data delivery or ordering which works well for broadcasting
			- other protocols like TLS encryption and WebSockets build off of TCP bc its fast and reliable
		- HTTP (hypertext transfer protocol)
			- lets applications view and modify data over the network
			- corresponds to the application layer of TCP/IP and application layer of OSI
			- using HTTP/HTTPS, clients make coded requests to servers which send back coded responses, where HTTP requests and responses are divided into the header which contains request metadata and the body which contains formatted data like JSON data
			- HTTP uses uniform resource identifiers (URLs) for users to specify what data they're trying to access
			- the codes in HTTP requests and responses communicate the kind of request or response
			- HTTP verbs specify what kind of request is being made
				- GET to read data, POST to create data in the body, PUT to create/update data with the data in the body, DELETE to request deletion of data, OPTIONS to list supported HTTP methods
			- HTTP status codes indicate the type of response being sent back
				- 1xx informational response, 2xx successful response, 3xx redirection response, 4xx client error response, 5xx server error response
			- HTTP includes sessions which can be established and maintained either server side or client side with HTTP cookies, and HTTP supports authentication

	- proxies
		- a proxy is a server or program between a client and application server to provide some intermediary sesrvice to the communication
		- forward proxy: a forward proxy is between clients and the public internet, with a goal to protect the client pool by filtering outgoing requests and incoming responses
			- used to enforce terms of use on a network, blocking malicious websites, and anonymizing network traffic using the IP address of the proxy instead of the client
		- reverse proxy: a reverse proxy is between the public internet and a pool of servers. because of its location as an intermediary, reverse proxies can anonymize cluster servers, terminate SSL, load balance, cache, filter requests, and prevent attacks like DOS detection
			- for example a reverse proxy can filter out non-GET requests before passing the requests on to the servers that handle the requests, to expose an API that is read-only
			- a reverse proxy could also terminate TLS so the application servers dont have to handle encryption/decryption, then pass on the requests within a private network so its still secure

- databases

	- types of database index
		1. Clustered Index
			- Sorts and stores the data rows in the table based on the key values. A table can have only one clustered index because the data rows themselves are sorted in this order, Ideal for columns that are frequently used in range queries or sorting (e.g, primary keys).
		2. Non-Clustered Index
			- Contains pointers to the actual data rows in the table. A table can have multiple non-clustered indexes, Best for columns used in search conditions or joins but not for sorting.
		3. Unique Index
			- Ensures all values in the indexed column(s) are unique, Useful for enforcing uniqueness constraints (e.g, email addresses).
		4. Composite Index
			- An index on two or more columns, Useful when queries filter or sort by multiple columns.
		5. Full-Text Index
			- Supports full-text queries on character-based columns, Ideal for searching large text fields (e.g, product descriptions).
		6. Spatial Index
			- Optimized for spatial data types like geometry or geography, Used in applications involving spatial queries (e.g, GIS systems).
		7. Filtered Index
			- A non-clustered index with a WHERE clause to filter rows, Useful for indexing a subset of data to improve performance.
		8. XML Index
			- Used to index XML data stored in a column, Optimizes queries on XML data.
		9. Columnstore Index
			- Stores data in a columnar forma, optimized for analytical queries, Ideal for data warehousing and large-scale analytics.

	- ACID database transaction processing
		- atomicity: all operations in a transaction are completely successfully or all fail
		- consistency: a transaction brings the db from on valid state to another
		- isolation: transactions are executed in isolation from one another, preventing concurrent transactions from impacting each other
		- durability: once a transaction is committed, it remains committed even in a system failure

	- DBMS
		- DBMSs are made to be fault-tolerant and scalable, offering a uniform method of accessing data across applications, and allow changing data storage by adding/removing discs while other system components are in operation
		- DBMSs have a presentation tier that forwards requests to the application tier, an applicationi tier that processes requests and manaages communication between other tirs, and a database tier that manaages data and maintains security/integrity and ensures efficient data retrieval and storage
		- data abstraction has a physical level describing how data is stored, a logical level describing what data is stored and data relationships, and a view level showing data from user perspectives
		- cardinality types include one-to-one, one-to-many, and many-to-many, describing quantities between data entities
		- there can only be one clustered index per table, as clustered indexes define the order of physical records and optimize for sequential access, whereas non-clustered indexes point to records and keep their pointers separate and optimize for queries on individual columns although non-clustered indexes require more space
		- commit writes transaction changes to disk ensuring durability
		- rollback erases all changes since the transaction started, maintaining consistency in case of failure
		- savepoint creates checkpoints in a transaction to allow rolling back to that point
		- hashing converts search keys to direct storage addresses, enabling fast data retrieval
		- inner join returns matching records, left outer join returns all records from the left and matching records from the right, full outer join combines all records from both tables, matching where possible, cross join produces a cartesian product of the two tables
		- memory alignment aligns the data memory block storage and its access 
		- referential integrity ensures there are no orphan foreign key values, which prevents modifying primary keys if theyre used as a foreign key
		- entity integrity ensures the primary key is not null
		- olap is online analytical processing for data warehouses dealing with large numbers of complex queries, oltp is online transaction processing dealing with large numbers of small transactions of standardized queries which is faster and uses databases
		- select into creates a temporary table in a sql query
		- GROUP BY summarizes data with equal values and uses HAVING to filter instead of WHERE, where HAVING filters aggregated values
		- a checkpoint is an event triggered when the database reaches a point in its performance history, events such as ensuring data is correct
		- sql correlated subqueries allow querying data already queried
		- physical, logical, and view schemas are different types of schemas in databases, where the physical schema is the actual database layout, the logical schema is a representation of the data, and a view schema is a subset of the database for a specific purpose, which can have types like relational, object-oriented, and xml

	- db normalization
		- eliminates insertion/update/deletion anomalies, improves data consistency, so one piece of data is stored in one place reducing the chances of inconsistent data
		- reduces data redundancy by dividing it into multiple related tables
		- improves query performance
		- but also increases complexity, reduces flexibility, and adds performance overhead by requiring joining tables
		- first normal form: each cell contains a single value and records are unique
		- second normal form: removes partial dependencies by separating tables, removes redundant data and places it in separate tables, requiring non-key attributes to be functional on the primary key
		- third normal form: ensures non-key attributes are independent of each other which eliminates transitive dependency
		- boyce-codd normal form: refinement of 3F that requires every determinant to be a candidate key
		- fourth normal form: addresses multi-valued dependencies, ensuring there are no multiple independent multi-valued facts about an entity in a record
		- fifth normal form (protection join): relates to reconstructing info from smaller, differently arranged pieces of data
		- sixth normal form: relates to temporal data (handling changes over time) by decomposing tables further to eliminate all non-temporary redundancy
		- denormalization combines tables to reduce the need for joins to optimize for fast data retrieval, though it makes updates harder bc data can be stored in multiple places and increases storage requirements

	- CAP theorem: any distributed database can only have two of three of the following:
		- consistency: every node provides the most recent data
		- availability: any node can respond
		- partition tolerance: the system works even if communication between nodes breaks down
		- partition tolerance is non-optional so there is a trade-off between consistency and availability
			- if a system goes down, the system can satisfy consistency by rolling back unfinished operations and waiting to respond until all nodes are stable again, or it can satisfy availability and continue to respond but risk inconsistencies
		- a CP database provides consistency and partition tolerance and an AP database provides availability and partition tolerance
		- CP databases sync data then send responses, and AP databases send responses then sync data
		
	- transactions: series of database operations that are treated as a single unit of work, where the operations must all succeed or all fail, which supports data integrity when a system fails
		- atomicity: all operations succeed together or fail together
		- consistency: a successful transaction puts the database in a valid state like with no schema violations
		- isolation: transactions can be executed concurrently
		- durability: a committed transaction is persisted to memory
		- not all databases support ACID transactions, relational database usually support ACID transactions and non-relational databases usually dont
	
	- schema: definse the shape of data structure and specifies what data can go where, specifying tables, indexes, and field types
		- schemas can be strictly enforced across the entire database, loosely enforced on part of the database or might not exist at all, there can be one schema for the whole database or different entries can have different schemas
		- a strictly enforced schema has the advantage of guaranteeing that queries will return data conforming to the schema, though these guarantees are computationally expensive as they have to be confirmed at every transaction and are difficult to scale especially if the schema specifies how data entries can reference each other, where maintaining these constraints are more difficult, as the reference span clusters and schema rules need to be verified across the network
	
	- scaling: vertical scaling adds compute/CPU and memory (RAM, disk, SSD) resources to one computer, where horizontal scaling adds more computers to a cluster
		- vertical scaling has much lower memory capacity, but horizontal scaling has much higher compute and storage capacity and can be sized dynamically without downtime, however relational databases struggle to scale horizontally
	
	- relational databases (mysql, postgresql, oracle) use a relational data model that organizes data in tables with columns of specific data types, where relationships between tables use foreign key columns that reference primary key columns of other tables
		- relational data models strictly enforce constraints to make sure data values and relationships are always valid against the schema, almost always using ACID transactions to ensure schema conformance
		- relational databases are also called sql databases
		- sql is declarative (the requesting entity tells the database what it wants and the database query planner specifies how to get that data)
		- tuning the query planner is one of the primary optimization techniques for relational databases
		- indexes allow frequently accessed columns to be grouped in a separate table with a foreign key reference to the original table, speeding up searches using those indexed columns
		- specially ordering data structures in indexes can make access faster, though writes are slower because each index needs to be updated in addition to the primary table
		- relational databases are almost always CP databases because guaranteeing consistency is important for the relational model to make sure that regardless of transactions the database is always in a valid state
		- relational databases are best when there are many-to-many relationships between entities, data needs to follow the schema, and relationships between data need to be accurate at all times
		- relational databases are hard to scale over distributed clusters (horizontal scaling) bc no matter how the data is split, there will be relationships between data entries on different nodes
		- relational database nodes need to communicate to normalize (sync) the data, so operations are slower because network communication is slower
		- relational databases arent useful if the data doesnt have many references, doesnt conform to a schema, or changes structure frequently
		- some databases implement multi-model support, supporting both relational and non-relational models
	
	- non-relational databases (NoSQL databases) are optimized for use cases that need scalability, schema flexibility or specialized query support
		- non-relational databases can use other query languages than sql but often implement sql or sql-like query support for developers
		- non-relational databases are either AP or CP databases given the use case theyre optimized for
		- with AP non-relational databases, eventual consistency is used to ensure that consistency still happens even if its not guaranteed after every transaction
		- graph databases (neo4j, cosmosdb) have nodes and edges and are good at representing data with relationships, similar to a relational database
			- in a graph database, queries dont need joins to follow relationship connections because data isnt stored in tables, so theyre suitable for queries that traverse many connections of a graph like social network analytics
		- document stores (mongodb, couchbase, firebase, couchdb, dynamodb) are usually simple JSON objects with a key identifier
			- in a relation database documents could be stored in multiple different tables, but a document store might store all relevant info for a user in one document so only one document needs to be accessed at a time
			- documents can have a variety of schemas which makes it easy to update or create a document without updating the entire database schema
		- a key value store (redis, dynamodb, cosmosdb, memcached, hazelcast) is similar to a document store but data stored in the value is opaque, so the key value store has no idea what is stored in the value, as it only provides read/overwrite/delete operations
			- there are no schemas, joins, or indexes, its more like a large hash table, and because of this, key value stores are scalable and particularly useful for caching
			- when the values are large, key value stores are called an object or blob store, in which case the data might be serialized and optimized for large file sizes
		- column-family database (cassandra, hbase, cosmosdb): a column family is a set of columns typically retrieved together, modeling data in tables like a relational database but storing column families together in files instead of rows and without enforcing relational constraints
			- this model boosts performance by limiting how much data needs to be read for data with strong column-family access patterns, and since columns tend to hold repeating info types, they can be compressed to save space which is helpful if data is sparse
			- this model might group name columns so regardless which components of a name a record has, all the name fields will be retrieved together, which also partitions the data table for horizontal scaling
		- search engine database (elasticsearch, splunk, solr): provides specialized feature of full text search over large amounts of unstructured text data, possibly from multiple sources and possibly also supporting fuzzy search where results may not be an exact match for the search string
			- useful for searching documents like system logs
		- time series database (influxdb, kdb, prometheus): optimized for data entries that need to be ordered by time, useful for storing real time data streams from system monitors such as errors
			- time series databases are write heavy and usually provide services for sorting streams as they come in to make sure theyre appended in the correct order, where these databases can be easily partitioned by time range
		- as scale becomes more important, relational databases can be too expensive so parts of the system can be moved to non-relational alternatives if they dont need strong schemas and consistency guarantees

	- database sharding
		- a technique for horizontal scaling of databases where data is split across multiple database instances or shards on separate servers to improve performance and reduce the impact of large amounts of data, where each row appears in one shard and each shard has the same schema
		- shard keys need to be unique across shards, which has a tradeoff between centralized name servers that can optimize logical shards for performance and a distributed algorithm that is faster to compute
		- shards can be configured to be optimized for usage patterns, actual shard sizes, etc
		- key based sharding (hash based sharding): columns are used to create a hash that is used to identify which shard data should be stored on using a modulus operation, which is useful for the predictable, uniform, and consistent data distribution, and can be optimized to handle range queries efficiently, but if the key is not well-distributed it can result in uneven data distribution and has limited scalability if certain keys are used more often or if the dataset is skewed toward specific key ranges, and selecting an appropriate key is complex and essential for effective key-based sharding, and adding shards using hashing can require a lot of overhead, which is limited by consistent hashing by guaranteeing a minimum of data will need to be moved when a new node is added
		- horizontal or range-based sharding: divides data by separating it into parts based on range of a value in each record, which has good scalability and improves query performance through parallelization, but coordinating queries across shards can be complex and poorly managed uneven data distribution may lead to uneven queries across shards
		- vertical sharding: splits columns of a record into separate shards, which improves query performance by allowing each shard to focus on a specific subset of columns which is efficient if queries only use those columns and simplifies queries that require only columns on one shard, but has a potential for creating shard hotspots if they contain highly accessed columns leading to uneven distribution of queries across shards, and making changes to schema is more complex using vertical shards
		- directory based sharding: creates and maintains a lookup table for the original database where a shard key corresponds to values in a column that is used as the mapping for identifying the shard a record is on before querying that shard, which allows for flexible data distribution where the central directory dynamically manages and updates the mapping of data to shard locations, allows efficient query routing to the appropriate shard using the information in the directory resulting in improved query performance, and can dynamically scale by adding or removing shards without requiring changes to application logic, but has a centralized point of failure in the lookup table and has increased latency by introducing another layer to each query
		- database sharding can be optimized for even data distribution with consistent hashing, choosing a well-balanced sharding key that doesnt create hotspots, making sure ranges are defined to balance data across servers if using range-based sharding, rebalancing shards when data distribution changes to avoid uneven loads, and automatically distributing data and handling sharding with database tools to maintain balance across shards
		- alternatives to database sharding include vertical scaling by adding CPU/memory/storage, replication to create copies of the database on multiple servers which helps with load balancing and ensures availability but can lead to synchronization issues, partitioning which splits data on the same server which improves query performance for large datasets, caching data to reduce load on the database, and creating CDNs for read-heavy workloads
		- sharding improves performance, scalability, can handle more traffic, improves resource utilization reducing the possibility of overloading a server, allows for fault isolation by isolating shards so one failure doesnt take down the system, and is cost efficient by allowing smaller cheaper servers to fulfill queries
		- but sharding is more complex than a single database, has rebalancing challenges, can handle cross-shard queries slower, requires more monitoring/backups/maintenance, and allows for the possibility of data loss if a shard fails and isnt backed up
		- denormalization is the process of ensuring there aren't relational constraints between different shards, which is achieved by duplicating and grouping data (like duplicating messages for each user on different shards) so the data can be accessed in a single row
		- if denormalization isnt possible and cross-shard queries are required, the consistency and availability trade-off applies
		- sharding is useful when a database server cant hold all the data, cant compute all the query responses fast enough, and cant handle the number of concurrent connections, and when its required to maintain different geographic regions
		- eventual consistency for duplicated data or upholding relational constraints must be implemented, and also failovers/backups/maintenance is more complicated

- latency and throughput and availability
	- latency is the time it takes a single request to travel from its point of origin to its destination and receive a response, combining response time, transmission time, queueing time, human reaction time, updating requester time, and processing time into round trip time, can be measured in seconds/milliseconds/nanoseconds
		- network latency: how long it takes data to move between two points in a network
		- system latency: the time it takes for a request to travel to its destination and receive a response
		- high latency can be caused by high network traffic, bandwidth limitations, geographical distance, server overload, and latency in database queries
		- adding an index or using a different database model can improve query latency
		- optimizing paths by minimizing the number of nodes a request has to travel through can improve network latency
		- caching can improve latency but can also increase it if poorly implemented
		- protocol choice like HTTP/2 can reduce the amount of protocol overhead for a request and can lower latency, and TCP has congestion avoidance features that can minimize congestion causes of latency
		- latency measuring tools
			- ping measures the round trip time, providing an estimate of network latency, by checking whether a node is reachable, sending a packet to a device and waiting for a response
			- traceroute displays the path that data packets take to reach a destination, identifying which network hops contribute to latency
			- MTR (traceroute with ping) combines traceroute and ping functionality, showing routing information and RTT at each hop on the path
			- performance profiling tools track resource usage and execution times within a system, providing detailed insights into system latency contributors
			- application performance monitoring (APM) tools monitor application performance including response times and latency across components
			- one-way latency is calculated as distance/propagation speed and RTT is twice the one-way latency
	- throughput is the rate at which a system/process/network can move data or handle operations in a particular period of time, measured in bits per second/bytes per second/transactions per second, etc, which is computed by dividing the total number of operations or objects executed by the time taken
		- network throughput: the quantity of data that can be sent via a network in a specific amount of time, which helps evaluate effectiveness of communication routes
		- disk throughput: the speed of data reads/writes to a storage device in bytes per second
		- processing throughput: the number of operations completed in a unit of time like the number of instructions executed per second, such as operations completed by a CPU or processor
		- latency is inversely related to throughput, and throughput is the actual amount of data transmitted in a time period and is not the theoretical capacity/bandwidth of the system
		- for example, latency is how long it takes to go from point a to point b, bandwidth is how wide the communication channel is, and throughput is how much data is transmitted in what amount of time
		- a network with high throughput can transfer large amounts of data quickly, where low latency means a minimal delay between request and response
		- throughput reflects system capacity and ability to handle multiple tasks at once, where latency reflects responsiveness and perceived speed of the system by the user
		- protocol overhead (like handshakes), high network traffic, bandwidth limitations, hardware performance, software efficiency and latency can all impact throughput
		- network optimization like optimal routing algorithms and efficient network protocols, load balancing, hardware upgrades, software optimization, protocol choice (TCP's congestion avoidance features), compression, improving latency, and caching can all improve throughput
	- availability is the amount of time that a system can respond, as in the ratio of uptime/(uptime  downtime), which is an important metric bc downtime can harm users, where 99.999% is the gold standard of uptime
		- hardware failure, software bugs, complex architectures with more points of failure making synchronization and fault tolerance difficult, dependent service outages, request overload, deployment issues can all impact availability
		- redundancy (failover systems, clustering, data backups/replication, geographic redundancy, automatic testing/deployment/rollbacks) is a solution to unavailability of a system

- load balancing
	- a load balancer is a network device or software application that distributes and balances and routes incoming traffic among servers to provide high availability/reliability, efficient usage of servers and high performance
	- without a load balancer, a server can be a single point of failure and the whole application can go down bc there is no load balancer to route requests to available servers, servers can be overloaded, and has limited scalability in that adding more servers is complex and wont help solve the load problem without a load balancer
	- load balancers enable horizontal scaling, ensure high availability/reliability, divide traffic among servers, optimize resource usage and prevent bottlenecks, monitor health of servers to direct traffic toward healthy servers, and handle SSL/TLS termination so servers dont need to have SSL/TLS connections
		- hardware load balancers are devices to control traffic distribution among servers, which are reliable but costly to scale and maintain, and are generally l4 transport layer load balancers since l7 decisions need to be updated more often
		- software load balancers (HAProxy, nginx) divide traffic among servers, running on existing infrastructure in contrast to hardware load balancers, and are more scalable and cheaper and more adaptable
		- cloud load balancers automatically divide traffic without requiring hardware, which is scalable and good for dynamic workloads as they can adjust to traffic spikes
		- dns load balancers integrate with DNS so a client's lookup for a service returns a different IP address to each requester from a pool of back-end servers in their geographic location
		- Layer 4 (transport) load balancers use IP addresses and port numbers (TCP/UDP) rather than the request content to divide traffic while operating at the OSI model's transport layer, which are quicker and useful for easy routing jobs bc they dont examine data being sent, managin high traffic with little overhead
		- layer 7 (application) load balancers function at the OSI model's application layer so they can route traffic according to request content including specific app data like HTTP headers, URLs, cookies, or user sessions, which are able to make complex routing choices like sending traffic to servers based on type of content or sending the same user to the same server for sticky sessions, l7 handles TLS termination so the TCP connection ends at the l7 load balancer
		- global server load balancers (GSLB) distribute traffic across servers in different geographical regions, routing requests to the closest or most responsive server, reducing latency and providing disaster recovery by ensuring service availability across multiple data centers in case of server or region failures
	- load balancing algorithms decide which request should be directed to which server
		- static load balancing algorithms involve predetermined assignments of tasks/resources without considering real-time variations, such as round-robin (requests are distributed equally), weighted round-robin (servers with more resources get more requests but without considering current server load or relative computation cost of requests), random request routing (weighted by server capacity, doesnt require coordination between multiple load balancers), and source IP/user/resource hashing (sends requests for the same IP/user/resource to the same server, which rebalances requests if an assigned server goes down which enables caching and server specialization and session stickiness which can only be implemented in l7 since it uses request content)
		- dynamic load balancing algorithms can direct requests to servers based on the distribution of incoming traffic or computing burden which adjusts to changes in resource availability, network traffic, and server load, like the least connection method or the least response time method, or the power-of-d choices algorithm which works with multiple load balancers
		- if the server pool resources and requests are similar and there is only one balancer, round robin is the default and works well, but if the server pool is different in computing power then round robin weighted by server capacity is useful, and if requests are different, least load methods are useful to prevent server overload, and when the system has multiple load balancers, the algorithm needs either a random or a power-of-d choice algorithm so the balancers dont all send traffic to the currently least loaded server at once
		- an l4 round robin load balancer can balance multiple power-of-d choices l7 load balancers
	- l7 load balancers terminate TCP connections and start a new connection which can also be encrypted, and load balancers protect against DDOS attacks by default
	- load balancers increase performance/scalability, efficient manage failure, prevent traffic bottlenecks, efficiently use resources, and maintain user sessions, enable horizontal scaling, dynamic scaling of server count in response to load, only requires knowing the address of the load balancer rather than the address of every server, improves throughput since availability and response times are not impacted by traffic, ensures a server cant be a point of failure using redundancy, and allows continuous deployment to deploy software updates without taking the system down and apply updates to one server at a time
	- but load balancers introduce a single point of failure, complexity/cost, configuration challenges, and can add latency, and can be challenging to implement SSL termination and end-to-end encryption and SSL inspection

- caching
	- stores frequently accessed data in a location that is easily and quickly accessible, acting as a local data store, to improve system performance by reducing access time of frequently accessed data
	- a web application may have an application server cahce and an in-memory store like Redis alongside the application server
	- a cache miss is where the call to the database is required
	- when a database query is performed, the request and result are saved in the cache
	- after the first database query, the application checks the cache first to see if the request has a result cached, if so it will request that result, which is known as a cache hit, and which will be quicker than the database query
	- all data isnt cached bc cache hardware is expensive compared to database storage, the search time will increase if all data is cached, cache is typically volatile storage so data is lost if the system crashes or restarts which would risk data loss if data was only stored in the cache
	- cache types
		- application server cache: a storage layer in an application server that temporarily holds frequently accessed data, which helps apps run faster, but with multiple servers, each server only knows about its own cache, resulting in cache misses so the data needs to be fetched frequently, which can be fixed by distributed caches or global caches
		- distributed cache: each node has a part of the cache space and using the consistent hashing function, each request is routed to where the cache request can be found
		- private cache (memcached, redis): exists in the memory of each app server in the service cluster, where since each machine stores its own cache data can get out of sync, but in-memory distributed caches are faster than shared caching layers requiring network requests
		- shared cache: a shared cache is in an isolated layer, where the cache and application layers can be scaled independently as the application only needs to be aware of the cache to detect cache availability so it can switch to the primary data store if the cache is down, and the shared and private caches can be used together where one can be a fallback in case the other cache fails
		- global cache: involves a single cache space where all the nodes use this single space and every request goes to this single space, where when a cache request isnt found, the cache has to find the missing data in the database/disk/etc, and where alternately the cache directly communicates with the database/server to fetch requested data
		- CDN: a group of servers placed across the globe to accelerate delivery of web content, managing servers that are geographically distributed, storing web content in its servers, and directing users to a server that is part of the CDN and close to the user to deliver content quickly, which is used when a lot of static content is served by the website like images or html/css/js, where if data isnt found, the CDN queries the backend servers and then caches the response locally
	- caching can be used for caching web page resources, database queries/data, in CDNs to keep copies of data in several places, in session caching to store session data to remember user info across visits to avoid re-logging in, and API response caching to reduce response time and reduce server load
	- caching improves performance, throughput, data retrieval times, reduces load on original data sources, and saves compute cost by improving efficiency of existing resources
	- but caching also can create data consistency issues, can cause performance issues/data loss if cache eviction policies arent designed correctly, and can add additional complexity to a system
	- caching requires cache invalidation/expiration/retention policies when data needs to be updated/deleted, which can be done with time-based expiration where cached data is discarded after a certain time (time to live TTL after which a resource is freed if it hasnt been used), and event-driven invalidation triggered by changes in data
	- eviction policies decide which existing item to remove when the cache is full and new items need to be stored, where the least recently used (LRU) policy eliminates the least recently accessed item, the least frequently used (LFU) policy removes the least frequently accessed items, and the First in, First out (FIFO) policy removes the oldest cached item
		- a least frequently recently used policy combines LRU and LFU, moving to LRU if data is used frequently enough
		- ARC (adaptive replacement cache) applies the LRFU approach and dynamically adjusts the amount of cache space based on recent replacement events, outperfoming LRU and LFU but requiring additional complexity, which is valuable when access patterns vary
	- caching is based on locality, in which programs access data repeatedly when the data is close, including temporal locality (data that has been referenced recently is likely to be referenced again) and spatial locality (data stored near recently referenced data is also likely to be referenced)
	- for example CPU has a cache in SRAM memory on the processor so it doesnt have to travel all the way to RAM/disk
	- caching is useful when data is slow to access, where there are many requests to static or slowly changing data, and useful to reduce load on primary data stores
	- caching isnt useful when accessing the cache and data takes similar amounts of time, when requests have high randomness/low repetition, and when data changes frequently
	- data that is mapped to a single cache entry is a direct-mapped cache, but if too many pieces of data are mapped to the same location, the resulting conflict increases cache misses bc relevant data is replaced too soon
		- the solution to this problem is using a set-associative cache design, where each piece of data is mapped to a set of cache entries which are checked to determine a cache hit or miss, which is slower than checking a single entry but provides flexibility in choosing what data to keep in the cache
	- caches can be seeded with relevant data to make it more useful at startup time, where this data can be predicted based on usage patterns or relevance scores
	- a write-behind cache writes to the cache first, then the primary store right away or when the cache entry is replaced at which point its tagged with a dirty bit to track data that is not synced, which on cache failure can result in data loss, though writes are faster in a write-behind cache
	- a write-around cache writes directly to the primary data store and the cache checks with the data store to keep the cache valid, where if the application is accessing the newest data, the cache might be behind, but the write doesnt need to wait on both systems being updated and the primary data store is always updated
	- a write-through cache updates both the cache and primary data store at the same time, so if the cache layer fails, the update isnt lost, though the writes take longer bc it needs to update the slower memory

- polling, websockets, and SSE
	- polling, websockets, and server sent events can all stream high volumes of data to/from servers
	- HTTP requests will slow down performance in cases like sending continuous information streams or real-time updates
	- polling, websockets, and SSE optimize speed and memory efficiency for data streams
	- short polling: original polling protocol to get regular updates from a server, starting by sending the server an HTTP request for new information, after which the server responds with new info or no info, and the client repeats this request at an interval, which has the advantage of being simple and widely supported bc its part of HTTP, but it has a lot of request overhead from both sides, the client has to make a lot of requests and the server has to handle a lot of requests
	- long polling: a more efficient type of polling where the client sends the server an HTTP request for new info, after which the server waits until theres new info to send back, and the client repeats the request as soon as it receives info back from the server, which decreases the number of HTTP requests necessary to transmit the same data to the client, where the server has to be able to hold unfulfilled client requests and handle the case where it gets new info but the client hasnt sent a new request yet, which is useful bc its part of the HTTP protocol so its widely supported and produces less traffic than short polling, which requires slightly more complexity than short polling but less complexity than websockets and SSE, but holding unfulfilled requests can take more resources than short polling and limit the number of possible connections, and message ordering cant be guaranteed and messages can get lost if there are multiple open requests from the same client, and long polling wont handle high volume data streams and is slowed down by repeatedly reestablishing a connection between server and client
	- SSE provide a one-way connection for a server to push new data to a client without reestablishing a connection every time, which follows the EventSource interface that uses HTTP to make the underlying communications, which first creates a new EventSource object targeting the server, the server then registers the SSE connection and sends new data to the client, the client receives messages with EventSource handlers and either side closes the connection, which is useful for creating an efficient one directional data stream without reestablishing a new connection and is simple to implement compared to websockets, but if the service requires more resources than the one-way connection model, it will be necessary to switch to websockets, and SSEs over HTTP instead of HTTP/2 are also limited to 6 connections per browser, which is useful when the client just needs to receive updates without communicating much with the server, but if more functionality like bi-directional communication is needed, websockets is more useful
	- websockets is a two-way message passing protocol based on TCP L4 of OSI, which are faster for communication than HTTP bc it has less protocol overhead and operates at a lower level in the network stack, where first the client and server establish a connection over HTTP and then upgrade using the websockets handshake, after which websockets TCP messagges are transmitted in both directions over port 443 or 80 if not TLS encrypted, then either side closes the connection, which is useful for speed as the client and server dont need to find and reestablish a connection every time a message is sent and data can flow immediately and in either direction once the websocket connection is established, and TCP ensures the messages will always arrive in order, but it takes a lot to implement such features as automatic reconnection, and websockets functions over ports so it can be blocked by firewalls

- queues and pub/sub
	- queues and pub/sub both allow a system to process messages asynchronously, allowing the sender and receiver to work independently by providing a middleman which can eliminate bottlenecks and help the system operate more efficiently
	- middleware is a system layer that provides commonly needed functionality as a service so developers can focus on functional or logical system components, which can be just a portion of the code or a server cluster, where middleware commonly provides translation, transaction processing, metrics monitoring, and message passing
	- messaging-oriented middleware enables communication between different components running different hardware/software, where producers hand off packets of data called messages to the messaging-oriented middleware which ensures the messages are delivered to the correct consumers, which allows asynchronous communication, where a producer sends messages independently of the state of the consumer, where if the consumer is busy or offline, the messaging-oriented middleware ensures the messages are delivered once the consumer becomes available again
	- asynchronicity allows components to be decoupled which adds resilience as when one component fails, the others can continue functioning normally, which also adds data integrity bc successful message passing isnt dependent on the producer and consumer being responsive at the same time
	- software that implements messaging-oriented middleware is called a message broker, which can implement one or several kinds of message passing including queues and pub/sub
	- message queues are a type of messaging-oriented middleware where producers push new messages to a named FIFO queue which consumers can then pull from, which is called point-to-point messaging bc there is a one-to-one relationship between a message's producer and consumer, where there can be many producers and consumers using the same queue but any particular message will only have one producer and one consumer
		- different queue implementations vary in how much space the queue has, whether messages are batched, and how long a message is kept for if it isnt consumed
	- the publish/subscribe pattern called pub/sub is a kind of messaging-oriented middleware that pushes a producer's newly published messages based on a subscription of the consumer's preferences, which has a one-to-many relationship between publishers and subscribers so any number of subscribers can get a copy of a message but theres only one publisher of that message, where pub/sub doesnt guarantee message order just guarantees that consumers will only see messages theyve subscribed to, where subscriptions can be filtered by topic/content, where topics are categories defined by the publisher and content is any category defined by a subscriber, which is up to the message broker to accept and manage these filters
	- how many message consumers the system has determines whether to use queues or pub/sub: if a message needs only one consumer then a message queue is useful, but if a message needs to have many consumers that all get a copy the pub/sub approach is useful
	- some features of message brokers include persistence where the messages are saved to persistent storage so they can be recovered if the message broker goes down, replays where messages are stored even after consumption so a service can replay the message stream in failure cases to recover, and ordering where the messages arrive to the consumer in a particular order

- scalability
	- scalability is the capacity of a system to support growth or manage increasing volumes of work with increased performance, efficiency, dependability, and availability
	- vertical scaling boosts server capacity with more CPU/memory/storage which is limited bc hardware cant always be upgraded more, horizontal scaling adds more servers/instances, divide and conquer breaks the app into microservices which are scaled as needed when one microservice is used more, and serverless automatically handles scaling like with AWS lambda
	- factors that can impact scalability include: performance bottlenecks (slow queries, inefficient algorithms, resource contention), efficient resource utilization to avoid bottlenecks and scaling limits, network latency which can delay communication between nodes, the way data is stored/accessed like with distributed databases and caches, concurrency/parallelism which can increase throughput and decrease response times, and system architecture like how components are structured and connected, where using a modular loosely coupled architecture that can be scaled horizontally or vertically is useful for scalability
	- components that increase scalability: load balancers, caches, database replication, database sharding, microservices, data partitioning, CDNs, and queueing systems
	- adding extra resources is costly and more complex, and optimizing for low latency may reduce throughput and vice versa, and partitioning data can improve scalability by distributing data across nodes but balancing the partition size, minimizing data movement, and ensuring data locality are tradeoffs that are necessary to navigate with partitioning

- distributed systems
	- a distributed system distributes data and resources over several servers or locations, which enables better scalability and reliability since the system can function in a component failure, though distributed systems are more complex to secure and maintain
	- distributed systems involve resource sharing where any hardware/software/data can be used anywhere in the system, openness which involves allowing open improvements to the system by sharing it, concurrency where local systems have independent operation systems and resources so can perform concurrent operations, scalability as more processors communicate with more users, fault tolerance by operating even when failures occur, and transparency in which the complexity of the system is hidden from users and local systems are kept private
	- distributed systems have advantages like scalability as they can easily add more servers/nodes to handle increased demand without complex reconfiguration, reliability/availability/fault tolerance where other components can take over for a failed component, performance where workloads can be split across multiple nodes so tasks are completed faster, resource sharing where data/storage/compute power can be shared across nodes thereby increasing efficiency and reducing costs, geographical distribution where distributed systems can server global users by providing faster access to node resources based on location since nodes can be in different locations
	- distributed systems have problems like security since resources are shared across multiple nodes, and networking saturation if there is a lag in the network, and complex databases compared to centralized systems, and overloaded networks if every node tries to send data at once

- fault tolerance
	- fault tolerance in distributed systems is the capacity to keep operating smoothly despite failures in components, which is crucial for reliability/availability/consistency
	- by implementing redundancy, replication, and error detection, distributed systems can handle various failure types, ensuring uninterrupted service and data integrity
	- faults are weaknesses in the system or its components which can lead to error/failure, errors are incorrect results bc of faults, failures are outcomes where the assigned success metric is not achieved
	- fault tolerance is the ability to function properly even with failures
	- fault types
		- transient faults: occur once then disappear, are difficult to find but dont harm the system much, like processor faults
		- intermittent faults: occur repeatedly, such as when the server hangs up
		- permanent faults: remain until the component is replaced, which are easy to identify but very damaging, like a burnt-out chip
	- availability is where the system is available at any time, reliability is where the system works continuously without failure, safety is where the system is safe from unauthorized access even with failures, maintainability is how easily the failed node can be repaired
	- first fault detection occurs, then fault diagnosis, evidence generation, assessment, and recovery
	- types of fault tolerance
		- hardware fault tolerance: involves a backup plan for memory/disk/CPU/other hardware devices, including methods like fault-masking and dynamic recovery
		- software fault tolerance: software is used to detect invalid output, runtime and programming errors, using static and dynamic methods to detect and provide the solution, and involving adding additional data points like recovery rollback and checkpoints
		- system fault tolerance: stores the system checkpoints, the memory block, program checkpoints, and detects errors in applications automatically, providing the solution to errors, thereby being reliable and efficient
	- fault tolerance strategies
		- redundancy/replication: data is duplicated to ensure availability and durability, and components are duplicated so if one fails the others can take over like redundant servers, network paths, or services
		- failover mechanisms: active-passive failover is where one active component handles the workload and another passive component is on standby and takes over if the active component fails, where active-active failover is where multiple components handle workloads and share the load, where if one component fails the others continue to handle the workload
	- error detection techniques
		- heartbeat mechanisms send regular signals/heartbeats between components to detect failures, and checkpointing periodically saves the system state so if a failure occurs the system can be restored to the last saved state
	- error recovery methods
		- rollback recovery is where the system reverts to a previous state after detecting an error using saved checkpoints or logs, and forward recovery is where the system tries to correct or compensate for the failure to continue operating which may involve reprocessing or reconstructing data

- event-driven architecture
	- event-driven architecture is where system components communicate with each other by generating, identifying, and reacting to events, where components are independent so they can function without each other, where when an event takes place, a message is sent, prompting relevant components to respond, which enhances flexibility, scalability, real-time responsiveness, and decentralized communication which enhances reliability and simplifies maintenance
	- events are expressed as messages or signals that communicate specific info, where various sources like user actions or data changes can trigger events, and EDA often uses asynchronous communication allowing components to work independently and in parallel, where a pub/sub model manages events where individuals who produce them are publishing them and interested entities subscribe to them, and where events are grouped together into types like UserLoggedIn or OrderPlaced, and where events often include extra info in the payload that provides context, where components have specific handlers that determine responses to events, and events allow immediate reactions to changes which is ideal when responsiveness is required
	- the event source generates events, the event is the core unit of communication representing relevant occurrences or changes in state which are emitted by sources and can contain various info which is the primary way different components communicate, the event broker/bus enables communication between components by handling event distribution/filtering/routing, ensuring that events reach the right subscribers and promoting efficient interactions, and the publisher generates and sends events to the event bus and is responsible for emitting events when specific actions/conditions occur, translating changes in the system into actionable messages that can trigger responses, where a subscriber is a component that subscribes to particular event types, listening for relevant events on the event bus and takes action accordingly, allowing for a responsive architecture where components react dynamically to changes, and where the event handler is a piece of code linked to a subscriber that defines how to process received events, and the dispatcher routes events to event handlers, controlling how events travel through the system, and the aggregator combines related events to create one significant event which reduces complexity by simplifying management of multiple events which makes it easier for subscribers to process relevant info, and a listener actively monitors the event bus for events and reacts to events, often for specific event types so they respond promptly to changes relevant to their function
	- EDA is useful for real-time applications, where scalability is needed, where components are decoupled, where event processing is complex, and where diverse systems need to communicate
	- EDA enables flexibility/agility, scalability, real-time responsiveness, loose coupling, and enhanced modularity
	- but EDA comes with increased complexity, its complex to keep event order and consistency, its difficult to debug/trace, and event latency is an issue bc events are processed individually
	- EDA focuses on events that represent significant occurrences or state changes, where Message Driven Architecture (MDA) centers around the exchange of messages between components often using a message broken
	- EDA involves communication of components through events, and MDA involves communication using exchange of messages which can have a broader scope than events
	- EDA emphasizes the flow of events triggering actions, and MDA involves data flow based on exchange of messages between components
	- EDA promose loose coupling of components, and MDA aims for decoupling by relying on messaging middleware
	- EDA triggers events by specific occurrences or changes in the system, where MDA sends/receives messages based on the needs of the communicating components
	- EDA examples include order placement and sensor data updates triggering actions, and MDA examples includ message queues, pub/sub systems, and request/reply patterns
	- EDA is where components have event handlers respond to specific events, and MDA is where components may have message handlers or listeners to process incoming messages

- leader election
	- a leader node directs what the follower nodes work on, which is useful when nodes are equal, when the cluster requires coordination, or when a system executes many distributed writes to data and requires strong consistency where the leader is the source of truth on the most recent state of the system
	- leader election adds complexity, and leader nodes can be a bottleneck or temporary single point of failure, and can pass on bad decisions to follower nodes, and makes partial deployment and A/B testing more complex by requiring the whole cluster to follow the same protocols or be able to respond to the same leader
	- leader election algorithms select a leader which will regularly pass a healthcheck/heartbeat, and selects synchronicity based on the cluster requirements, so if messages dont need to be delivered in a specific timeframe or in a specific order then asynchronous cluster messages are acceptable, otherwise synchronous messaging is used, where in an asynchronous cluster nodes can lag indefinitely so the leader election cant guarantee safety (no more than one leader is elected) and liveness (every node finishes the election), so implementations choose guaranteeing safety which is more important, and where synchronous algorithms can guarantee safety and liveness but requires additional constraints on how the cluster operates that arent always possible or scalable
		- bully algorithm: synchronous leader election algorithm where the highest id node declares itself the winner and lower id nodes declare themselves the winner if requests to higher id nodes fail, which frequently re-elects the highest node id as the winner if it goes down frequently, and is difficult to maintain synchronization of messages as the cluster gets larger and physically distributed
		- paxos: asynchronous leader election protocol that uses state machine replication to model the distributed system, then asks some nodes to propose a leader where some nodes accept proposals and when a quorum of the accepting nodes choose the same leader, that becomes the actual leader
		- raft: asynchronous leader election protocol where nodes track the current election term, incrementing the election term when leader election starts, and listen for messages where after a random interval if no response is received, the node becomes a candidate and asks for votes, and if it reaches a majority of votes it becomes a leader and if it receives a messages from a higher term candidate it concedes, which restarts if the election is tied or times out without consensus
		- apache zookeeper: a centralized coordination service that uses zookeeper atomic broadcast (ZAB) an asynchronous algorithm to handle leader election, replication order guarantees, and node recovery, where the leader broadcasts state changes to followers to make sure writes are consistent and propagated to all nodes, which focuses on making sure the cluster history is accurate through leadership transitions, where the leader is chosen so that it has the most updated history (it has seen the most recent transactions), where when nodes agree that the new leader has the most updated history, it syncs history with the cluster and records itself as the leader
	- alternatives to leader election allow for the possibility that coordination is possible without a leader node
		- locking: ensures concurrent operations on a shared resource dont conflict by only allowing changes from one node at a time, where with optimistic locking a node will read a resource and its version id, make changes, then before updating make sure the version id is the same, if the id is different the resource has been updated since the node read it, so going forward with the intended chnages would lose other changes so the node needs to try again, and in pessimistic locking a node locks the resource, makes changes, and then unlocks the resource, and if another node tries to initiate a change while the resource is locked it will fail and try again later, which is more rigorous than optimistic locking but harder to implement and bugs can cause deadlocks that stop the system from functioning, where optimistic locking is useful when it can be assumed that another node wont change the resource at the same time, and pessimistic locking is useful when it can be assumed that there will be resource contention
		- idempotent APIs: APIs are idempotent when the same request sent multiple times wont produce inconsistent results, which means the response will always be the same value for read operations, and means an update will only happen once for write operations, which may implement a request id so the system can tell if a request is being retried, where idempotency is supported by locking and database transactions
		- workflow engines: another way of coordinating nodes in a system is by using a workflow engine, a centralized decision making system that contains a set of workflows of what work can be done, the state of data and work in the system, and the resources available to assign work to (like aws step functions, apache airflow)

- design patterns
	- creational design patterns help make a system independent of how its objects are created, composed, and represented
		- factory method: this pattern is useful to separate the construction of an object from its implementation, so objects can be created without having to define the exact class of object to be created
			- Factory easily adds new class types without changing existing code, avoids tight coupling between sub-classes/objects and creator classes/objects
			- But the client might have to sub-class the creator class and might create a large number of files
			- replaces the object construction calls with calls to the factory method
			- allows an interface or a class to create an object, but lets subclasses decide which class to instantiate
			- creates objects without exposing logic to the client and uses the same interface to create new objects
		- abstract factory method: another layer of abstraction over the factory pattern, which works with a super-factory that creates other factories
			- allows creating families of related objects without specifying their concrete classes, creating a similar type of many objects
			- provides a way to encapsulate a group of individual factories
			- replaces object construction calls with calls to the abstract factory method
			- useful when client doesnt know which type to create, makes it easy to introduce new variants of classes without breaking existing code, and classes created from the factory are compatible
			- But if there are a lot of classes code can become complex and create a large number of files
		- singleton method: the singleton pattern guarantees that a class has just one instance and offers a way to access it globally
			- a way to provide one and only one object of a type like a database connection which should only have one instance at a time
			- Borg singletons allow multiple instances with shared state
			- Double checked locking singleton only assigns a lock using the getinstance method when the object is None
			- classic singleton method uses the static method for creating the getinstance method to return the shared resource
			- the virtual private constructor __init__ can be used to raise an exception although its not required
			- an object created with singleton is initialized only when requested for the first time, and it grants global access to the instance of the object, and method classes cant have more than one instance
			- But it's difficult to use singletons in a multithread environment bc we have to guarantee that the multiple threads cant create a singleton object more than once, and singleton doesnt follow the single responsibility principle bc it solves multiple problems at once, and singleton makes unit testing harder by introducing global state
			- singleton is recommended where control over global variables is important and is often used in logging, caching, thread pools, and configuration settings and often used with the factory method
		- prototype method: allows hiding complexity of making new instances from the client, copying an existing object rather than creating a new instance
			- enables creating new objects by cloning existing objects (making the existing cloned object the prototype), which is efficient when the cost of creating a new object is high and when an object's initial state or configuration is complex
			- includes:
				- the prototype interface or abstract class that declares methods for cloning objects, defining the common interface that concrete prototypes have to implement so all prototypes can be cloned consistently, declaring the clone method to produce copies of the prototype
				- concrete prototypes is a class that implements the prototype interface or extends the abstract class, and is the class of the specific type of object being cloned, defining the details of how cloning should happen for instances of that class and implementing the clone method for specific cloning logic for that class
				- client is the code that requests the creation of new objects by interacting with the prototype, initiating the cloning process without being aware of the concrete classes involved
				- clone method is declared in the prototype interface or abstract class, and implemented in concrete prototypes to define specific cloning logic, describing how the object's internal state should be duplicated to create new independent instances
			- use the prototype method when creating objects is more costly or complex than copying existing ones, when objects need to vary slightly without justifying a whole set of alternate classes, when the system requires dynamic configuration and you want to create objects with configurations at runtime so prototyping a base configuration and cloning it would be useful, and when you want to reduce the cost of initializing an object
			- dont use the prototype method when object instances are unique and implementing the pattern costs more than it benefits, when object creation is simple and doesnt consume a lot of resources and there is no object variation required, when objects are immutable which are often safely shared without requiring cloning, when the object creation process is easy to understand and manage, when there are only a few variations of objects and creating subclasses or instances with specific configurations is easy
		- builder method: used to separate construction of a complex object from its representation so the same construction process can create different representations, helping construct a complex object step by step in which the final step returns the object
			- allows using the same construction code to create different types and representations of the object easily, designed to provide flexibility to solutions to various object creation problems
			- allows separating business logic and the complex construction code, and constructs objects step by step, allows deferring construction steps, allows calling steps recursively, prevents the client from fetching incomplete data bc it doesn't allow exposing an unfinished object, is useful when constructing various representations of the class involves similar steps that vary in details, in which case the base builder interface defines the construction steps while these steps are implemented by concrete builders
			- But increases code complexity bc it requires creating multiple new classes, requires the builder class to be mutable, and data members of the class arent guaranteed to be initialized
	
	- structural design patterns use inheritance to compose interfaces or implementations, solving problems of composing classes and objects into larger structures which are flexible and efficient
		- adapter method: converts the interface of a class into another interface expected by the client, letting classes work together that couldnt otherwise bc of incompatible interfaces
			- helps make incompatible objects adaptable to each other by creating a connection between two incompatible interfaces, providing a different interface for a class, thereby enabling integration of classes that were previously incompatible
			- the client requests to the adapter using the target interface, the adapter translates the request to the adaptee interface, then the result of the call is received by the client
			- for example, the adapter passes arguments like functions/attributes with different names by using the same parameter, so that same parameter can be used to access the function/attribute instead of the different function/attribute names
			- the adapter achieves single responsibility bc it separates specific code from primary logic of the client
			- the adapter is flexible and allows code reusability
			- the client class is not required to use a different interface thereby allowing the client to remain simple and we can use polymorphism to swap between different implementations of adapters
			- the new adapter classes can be introduced without violating the open/closed principle
			- But the adapter increases complexity of the code and requires many adaptation with the adaptee chain to reach the compatibility that we want
			- adapter is used when we want to make certain classes communicate
			- when we want to reuse some piece of code like interfaces that lack some functionality, the adapter method is used
		- bridge method: allows abstraction and implementation to be developed independently, so the client code can access the abstraction part without accessing the implementation part
			- allows separating implementation-specific abstractions and implementation-independent abstractions so they are developed as single entities, useful for organizing the class hierarchy
			- the abstraction provides the reference to the implementer
			- the refined abstraction extends the abstraction to a new level where it takes the specific details one level above and hides the specific elements from the implementers
			- the implementer defines the interface for implementation classes, which doesnt need to correspond directly to the abstraction interface and can therefore be very different
			- concrete implementation: the concrete implementation implements the above implementer
			- the implementation-specific abstractions are separated from the class with the implementation-independent abstractions, such as by passing the implementation-specific abstraction as a parameter to the class with the implementation-independent abstractions
			- the bridge method follows the single responsibility principle bc it separates abstractions from their implementation so the abstraction and implementation can vary independently
			- bridge doesnt violate the open/closed principle bc at any time, we can introduce the new abstractions and implementations independently from each other
			- bridge can be used to implement platform-independent features
			- But the bridge method is complex bc it introduces new abstraction classes and interfaces, and might negatively impact performance bc the abstraction has to pass messages along with the implementation for the operation to be executed, and is difficult to manage with many interfaces
			- the bridge method provides run-time binding of an implementation (run-time binding is what we can call a method at run-time instead of compile-time)
			- the bridge method is used to map independent class hierarchies
		- composite method: a partitioning design pattern which characterizes a collection of items that are handled the same as a single instance of that type of object, with intent to compose objects into tree structures to represent part-whole hierarchies
			- composite method describes a group of objects that is treated the same way as a single instance of the same type of object, with intent to compose objects into tree type structures to represent the whole-partial hierarchies
			- composite method allows composing objects into the tree structure and then allows working with tree structures as an individual object
			- the operations that can be performed on all the composite objects often have the least common denominator relationship
			- component: helps implement default behavior for the interface common to all classes, declaring the interface of the objects in the composition and for accessing and managing its child components
			- leaf: defines behavior for primitive objects in the composition, representing the leaf object
			- composite: stores the child component and implements child related operations in the component interface
			- client: manipulates objects in the composition through the component interface
			- the composite method is used when there are composites that contain components, each of which could be a composite
			- the composite method follows the open/closed principle bc the introduction of new elements, classes, and interfaces is allowed into the application without breaking the existing code of the client
			- the composite method allows consuming less memory bc it creates less objects and it has improved execution time by sharing objects, and is flexible by providing flexibility of structure as it defines class hierarchies with primitive and complex objects
			- But it makes it harder to restrict the type of components of a composite, and is not useful when representing a full or partial hierarchy of objects is not needed, and produces the general tree once the tree structure is defined, and depends on run-time checks to apply constraints bc it doesnt allow using the type system of the language
			- composite is preferred when producing a nested tree structure is required, and allows organizing structures with common operations so the structures can be handled in the same way
		- decorator method: allows dynamically adding functionality to an object without affecting the behavior of other existing objects within the same class, using inheritance to extend the behavior of the class which takes place at compile-time so all the instances of that class get the same extended behavior
			- allows functionality to be added to individual objects dynamically without affecting the functionality of other objects from the same class, which involves decorator classes which wrap concrete components
			- promotes flexibility and extensibility by allowing composing objects with different combinations of functionality at runtime
			- follows the open/closed principle since new decorators can be added without modifying existing code
			- decorators are used where a variety of optional features need to be added in a flexible and reusable manner
			- add additional functionality like cross-cutting variables such as logging, profiling, caching, error handling or authentication without modifying core logic
			- component interface: an abstract class or interface that defines the common interface for the concrete components and decorators, specifying the operations that can be applied to the objects
			- concrete component: these are the basic objects or classes that implement the component interface, they are the objects to which new behavior is added
			- decorator: an abstract class that also implements the component interface and has a reference to a component object, responsible for adding new behaviors to the wrapped component object
			- concrete decorator: these are the concrete classes that extend the decorator class, adding specific behaviors to the component, where each concrete decorator can add one or more behaviors to the component
			- unlike traditional inheritance which can lead to a deep and inflexible class hierarchy, the decorator pattern uses composition, allowing composing objects with different decorators to add the necessary functionality, which avoids the disadvantages of inheritance like tight coupling and rigid hierarchies
			- decorators allow dynamic behavior modification by allowing application or removal at runtime, which is useful to change object behavior based on changing requirements or user preferences
			- allows clear code structure
			- decorators can add complexity, increase the number of classes, increase requirements like managing the correct order of decorators, and overusing decorators is a complicating factor
		- facade method: provides a unified interface to a set of interfaces in a subsystem, defining a high-level interface that makes the subystem easier to use
			- helps reduce dependencies between clients and a system, making code more modular and understandable, allows hiding complexities of a system and offering a simpler way to interact with the system, enhancing maintainability and scalability
			- structuring a system into subsystems helps reduce complexity
			- minimizing the communication and dependencies between subsystems is useful
			- one way to minimize communication/dependencies between subsystems is a facade object that provides a simple interface to other functions of a subsystem
			- facade: a single class that provides a simple interface to a complex subsystem, which delegates client requests to the appropriate subsystem objects without exposing the underlying complexity
			- subsystem classes: classes that do the work of the system, which provide the actual functionality, which are not directly accessible by clients but are used by the facade
			- client: entity that interacts with the subsystem through the facade by making requests to the facade
			- used to simplify complex system, promote loose coupling, hide implementation details, improve code readability and maintainability, implement layers like the business logic layer and hiding the complexities of data access and processing layers, and manage legacy code
			- avoid the facade if abstraction is unnecessary, if direct access to subsystems is needed, to avoid performance hits by adding extra layers of method calls, when subsytems are simple, and when the facade is tightly coupled with client code so making changes to subsystems requires making changes to the facade and client, which defeats the purpose of decoupling, so that the facade becomes a bottleneck for changes and updates which hinders system flexibility
		- flyweight method: provides ways to decrease object count thereby improving applications' required objects structure, used to create a large number of similar objects
			- minimizes object count required at run-time, creating a flyweight object that is shared by multiple contexts, created to be indistinguishable from normal objects
			- flyweight objects are immutable
			- to implement flyweight, dictionaries store references to the objects that are already created
			- fewer objects reduce memory usage and reduces object creation time by sharing objects or sharing common parts of objects
			- flyweight uses less RAM, improves data caching for fast response time, and improves performance bc it uses less heavy objects
			- But flyweight breaks encapsulation by moving state outside the object which is less efficient, and flyweight complicates code
			- flyweight saves space when the application is independent of the object created, and reduces cost in terms of space and time complexity
		- proxy method: also called surrogates, handles, and wrappers, closely related in structure but not intent to adapters/decorators
			- allows providing a replacement for another object, using different classes to represent functionality of another class, creating an object having the original object functionality
			- proxy method controls and manages access to the object being protected
			- for example the proxy method can avoid multiple database connections, by making one proxy connection to the database which handles multiple queries
			- the proxy method follows the open/closed principle bc new proxies are easily introduced without changing client code
			- the proxy works even when the service object is not ready or not available, and the proxy method also provides security and increases performance by avoiding duplication of objects that can be large and memory intensive
			- But the proxy might create slow responses, and introduces another layer of abstraction which is a problem if the protected code is accessed directly by some clients and some of them use the proxy class, and increases complexity by introducing a lot of new classes
			- a virtual proxy is used in databases, a protective proxy creaets a protective layer over the application, a remote proxy is used when the service object is located on a remote server so the proxy passes the client request over the network, and a smart proxy provides additional security to the application by intervening with specific actions when the protected object would be accessed
	
	- behavioral design patterns relate to algorithms and the assignment of responsibilities between objects, describing not just patterns of objects or classes but the patterns of their communication, characterizing complex control flow that's difficult to follow at run-time
		- chain of responsibility method: used for loose coupling where a request from the client is passed to a chain of objects to process the request, and later the objects in the chain will decide who will be processing the request and whether the request needs to be sent to the next object in the chain
			- chain of responsibility is the object version of a set of if/elif/else conditions and allows rearranging condition-action blocks at run-time, allowing passing request along the chain of handlers
			- it decouples sender and receiver of a request, creating an abstract handler and a set of specific handler for sequential operations which should be performed dynamically
			- it follows the single responsibility principle by decoupling the classes that invoke operations from classes that perform operations
			- it follows the open/closed principle by introducing new code classes without breaking existing client code
			- it increases flexibility of the code while giving responsibilities to the objects
			- But chain of responsibility doesnt guarantee whether the object will be received, makes debugging difficult bc observing characteristics of operations is difficult, and might decrease performance bc of continuous cycle calls
			- chain of responsibility is useful when its required to process handlers in a certain order bc the linking is possible in any order, and when sender and receiver of request should be decoupled and when avoiding specifying handlers is useful
		- command method: transforms a request into an independent object with all of the information requested, an object which can be passed around, stored, and executed at a later time
			- encapsulates a request as an object, allowing parameterization of clients with different requests and the queuing/logging of requests
			- promotes the invocation of a method on an object to object status, encapsulating all the info to perform an action
			- suggests that objects shouldnt send requests directly but instead the request info should be moved to a separate command class with a method that triggers the request
			- follows the open/closed principle by introducing new commands without breaking existing client code
			- follows the single responsibility principle by decoupling classes that invoke operations from other classes
			- allows implementing undo/redo with the command method
			- allows encapsulating the info needed to perform an action
			- But increases complexity bc of the layers in between the sender/receiver, increases the quantity of classes, and every command is a ConcreteCommand class that increases the count of classes for implementation and maintenance
			- it implements reversible operations and is useful when its required to parameterize objects with the operations
		- interpreter method: used to define a grammatical representation for a language and provides an interpreter to deal with this grammar
			- enables interpretation and evaluation of expressions or language grammars, allows building an interpreter for a language using symbols or expressions, requiring defining a class for each symbol or expression and implementing an interpret method that evaluates these symbols
			- AbstractExpression is an abstract class or interface that declares an abstract interpret() method, representing the common interface for all concrete expressions in the language
			- TerminalExpression is the concrete class implementing the AbstractExpression interface, representing the terminal symbols or leaves in the grammar, which are the building blocks the interpreter uses to interpret the language
				- in an arithmetic expression interpreter, terminal expressions could include literals like numbers or variables representing numeric values
				- these terminal expressions would evaluate to their respective values directly without further decomposition
			- NonterminalExpression is a concrete class implementing the AbstractExpression interface, handling composite expressions which consist of multiple sub-expressions, tasked with providing interpretation logic for such composite expressions
				- their responsibility is also to coordinate the interpretation process by coordinating interpretation of sub-expressions
				- this involves coordinating interpretation calls on sub-expressions, aggregating results, and applying necessary modifications to achieve the final interpretation of the whole expression
				- non-terminal expressions enable traversing expression trees during the interpretation process
				- they recursively interpret sub-expressions, ensuring each part of the expression contributes to the interpretation
			- Context contains info that is global to the interpreter and is maintained and modified during the interpretation process, possibly including variables, data structures or other state info the interpreter needs to access or modify while interpreting expressions
			- Client is responsible for creating the Abstract Syntax Tree and invoking interpret() on the root of the tree, typically created by parsing the input language and constructing a hierarchical representation of the expressions
			- expression evaluators evaluate mathematical expressions, boolean expressions, etc
			- compilers and interpreters parse and interpret languages
			- command processors execute commands based on a defined grammar
			- use interpreter when its required to interpret or evaluate expressions repeatedlly and the grammar is stable and not too complex, when its required to represent a simple language grammar and its parsing directly in code, when its required to build a simple command processor or scripting language
			- dont use interpret when the language grammar is difficult and often changes, also interpreted languages are slower than compiled languages, and the interpreter could complicate error prevention and speeding up processes
		- mediator method: enables decoupling of objects by introducing a layer in between so the interaction between objects happen with the layer
			- promotes loose coupling between objects by centralizing communication between them, which is useful when you have a complex system with multiple objects that need to interact and its required to avoid tight coupling that can result from direct object-to-object communication
			- Mediator is an interface or class responsible for defining communication interface between objects, acting as a central hub for communication and containing method allowing objects to send and receive messages
			- Concrete Mediator is a specific implementation of the Mediator interface, managing the interactions between objects, knowing how to route messages and coordinate actions between objects
			- Colleague: colleagues are individual objects that need to communicate, are aware of the mediator but dont have direct references to other colleagues, instead sending/receiving messages with the mediator
			- reduces direct dependencies between objects, promoting a loosely coupled system, only requiring colleagues to know about the mediator which makes it more maintainable and extensible
			- centralizes communication which can simplify complex interactions, allowing enforcement of rules, coordination of actions, and organization of communication
			- mediators can be reused/applied to various situations to manage interactions between objects
			- isolates communication-related logic in one places, following the single responsibility principle
			- But introducing a mediator can add complexity if there are a small number of objects or if the interactions are simple, and can introduce performance hits since all messages pass through one central point, and requires maintaining the mediator which is challenging in a complex environment or with changing communication requirements, and can turn the mediator into a god object that knows too much about the system and handles too much logic
		- memento method: used to return an object's state to its initial state, enabling creating checkpoints in an application and returning to these checkpoints at a later time
			- allows capturing and restoring an object's state without violating encapsulation and without revealing its internal structure, which is useful when implementing undo/redo mechanisms, state persistence across transactions, encapsulation of state management, temporary state storage, snapshot management, and checkpoints in applications, allowing the system to revert to a previous state when needed
			- originator: the object whose internal state is to be saved and restored, creating a memento containing a snapshot of its current state and using the memento to restore its state later
			- memento: the object storing the internal state of the originator, containing a snapshot of the originator's state at a point in time, usually immutable to ensure state cant be modified once captured
			- caretaker: the object responsible for managing the memento, requesting a memento from the originator, holding the memento, and passing the memento back to the originator when needed for state restoration, without modifying or inspecting the contents of the memento
			- avoid the memento pattern if state management is simple and doesnt require frequent saving or restoration, to avoid high memory usage of mementos if the state is large or changes frequently, if there is no need for state restoration and for security concerns if the state contains sensitive info
		- observer method: establishes a one to many dependency between objects, meaning all the dependents (observers) of the subject are immediately updated and notified when the subject changes
			- allows defining or creating a subscription mechanism to send notifications to multiple objects about any new event that happens to the observed publisher object the subscribers are observing, where the publisher needs to be monitored and when there is a change in the publisher, the observers are notified about the change, defining a one-to-many dependency between objects so that when one publisher object changes state, all the dependent observers/subscribers are notified and updated automatically
			- follows the open/closed principle by introducing subscriber classes without making changes to the client code, establishes relationships between objects at run-time, and carefully describes the coupling present between the object and the observer so there is no need to modify the publisher to add/remove observers
			- But the observer method can cause memory leaks bc of explicit registering/unregistering of observers caused by the lapsed listener problem, and subscribers get randomly ordered notifications, and can increase code complexity
			- observer should be used when there are multiple objects dependent on the state of one object, and when notifications are needed
		- state method: where an object modifies its behavior according to its internal state, where if we have to change the behavior of an object based on its state, we can use a state variable in the object and an if-else condition to perform different actions based on the state
			- allows an object to change its behavior when there is a change in its internal state, which helps implement the state as a derived class of the state pattern interface
			- if its necessary to change the behavior of an object based on its state, there can be a state variable in the object and an if/else condition block to perform different actions based on state, which implements an object-oriented finite state machine, implementing state transitions by invoking methods from the pattern's superclass
			- suggests creating a new class for all possible states of an object and extracting all state-specific behaviors into these classes, where instead of implementing all behaviors on its own, the original object called context stores a reference to one of the state objects representing its current state and delegates state-related work to that state object
			- follows the open/closed principle allowing introducing new states without changing the content of existing states of the client code
			- follows single responsibility principle in organizing code of specific states into separate classes
			- improves cohesion since state-specific behaviors are aggregated into the ConcreteState classes which are in one location in the code
			- But the state method can make a system overly complex if there are just a few states, changes state at run-time, increases the number of classes, and each state-derived class is coupled to its sibling which introduces dependencies between sub-classes
		- strategy/policy method: selecting an object's behavior at runtime, involving encapsulating a family of algorithms into distinct classes that each implement a common interface
			- allows defining a complete family of algorithms, encapsulating each one and putting them into separate classes and allows exchanging objects, which is implemented by dynamically replacing the content of a method defined in a class with the contents of functions defined outside the class, enabling selecting the algorithm at run-time
			- follows the open/closed principle bc its easy to introduce new strategies without changing the client code
			- isolates specific details of the algorithms from the client code
			- encapsulates data structures for implementing the algorithm in strategy classes so the implementation of the algorithm can be changed without affecting the context class
			- allows switching strategies at run-time
			- But creates extra objects, creating both the context and the required strategy object, and differences in strategies should be clear to clients to select the best strategy, and increases complexity
			- strategy is preferred when there are a lot of similar classes that differ in how they execute, and is used to isolate business logic of the class from the algorithmic implementation
		- template method: defines an algorithm as a collection of skeleton operations where the child classes handle the implementation of the specifics and the parent class maintains the overall structure and flow of the algorithm
			- defines the skeleton of the operation and allows details to be implemented by the child class, where its subclasses can override the method implementations as needed but the invocation is the same as defined by the abstract class, allowing reusing the same code by making certain changes
			- provides flexibility since subclasses can decide how to implement the steps of the algorithms, and allows inheritance and therefore code reuse
			- But the code may become complex, and clients may request the extended version bc the skeleton template has too few algorithms, and by using the template method you may violate the liskov substitution principle
			- its useful when its required to let clients extend an algorithm, and when there are a lot of similar algorithms with trivial changes to avoid changing all algorithms when one change is required, and enables developing frameworks by enabling code reuse through making code changes
		- visitor method: used to perform an operation on a group of a similar kind of Objects, enabling moving the operational logic from the objects to another class
			- allows separating an algorithm from an object structure on which it operates, allows adding new features to an existing class hierarchy dynamically without changing it
			- is useful for handling communication between objects, like all other behavioral design patterns
			- visitor is used when its required to perform an operation on a group of similar kinds of objects
			- visitor consists of a visit method implemented by the visitor and used and called for every element of the data structure, and visitable classes providing accept methods that accept a visitor
			- client: consumer of classes of the visitor design pattern, accessing the data structure objects and instructing them to accept visitors for future processing
			- visitor: an abstract class used to declare visit operations for all visitable classes
			- concrete visitor: each visitor is responsible for different operations, where for each visitor all the visit methods declared in the abstract visitor must be implemented
			- visitable: accepts operations are declared by the visitable class, acting as the entry point enabling an object to be visited by a visitor
			- concrete visitable: these classes implement the visitable class and define the accept operation, the visitor object is passed to this object using the accept operation
			- the visitor method suggests adding new behaviors to a separate visitor class instead of mixing it with the already existing classes, so the original object is passed to the visitor method as a parameter so the method will access all the necessary info
			- follows the open/closed principle by making it possible to introduce new behavior in a class without making changes in these classes
			- follows the single responsibility principle in that multiple versions of the same behavior can be operated on the same class
			- adding an entity in the visitor method is easy since it requires changing the visitor class only and not affecting existing items
			- updating logic only requires changing the visitor implementation rather than changing all the item classes
			- But every visitor needs to be updated when a class is added or removed from the hierarchy, and if there are too many visitor classes its hard to extend the interface, and visitors might not have access to private fields of classes theyre supposed to work with
			- visitor method works well with recursive structures like directory trees or xml structures bc it can visit each node in the recursive structure, and the visitor method is useful when performing operations on all elements of the complex object like a tree

- Cloud Native Distributed System Design Patterns: priority queue, api routing, retry, rate limiting, failover, circuit breaker, sharding, throttling, health endpoint monitoring, index table
	Pattern							Summary
	Ambassador						Create helper services that send network requests on behalf of a consumer service or application.
	Anti-Corruption Layer			Implement a façade or adapter layer between a modern application and a legacy system.
	API routing 					Path routing, hostname routing, HTTP header routing
	Asynchronous Request-Reply		Decouple back-end processing from a front-end host. This pattern is useful when back-end processing must be asynchronous, but the front end requires a clear and timely response.
	Backends for Frontends			Create separate backend services for specific frontend applications or interfaces.
	Bulkhead						Isolate elements of an application into pools so that if one fails, the others continue to function.
	Cache-Aside						Load data on demand into a cache from a data store.
	Choreography					Let individual services decide when and how a business operation is processed, instead of depending on a central orchestrator.
	Circuit Breaker					Handle faults that might take variable time to fix when an app connects to a remote service/resource, wrapping services so when the service fails the 																					circuit break is activated, so future calls fail fast instead of trying to connect to a failing service repeatedly, preventing cascading failures
	Claim Check						Split a large message into a claim check and a payload to avoid overwhelming a message bus.
	Compensating Transaction		Undo the work performed by a sequence of steps that collectively form an eventually consistent operation.
	Competing Consumers				Enable multiple concurrent consumers to process messages that they receive on the same messaging channel.
	Compute Resource Consolidation	Consolidate multiple tasks or operations into a single computational unit.
	CQRS							Command Query Responsibility Segregation: Separates operations that read data from those that update data by using distinct interfaces.
	Deployment Stamps				Deploy multiple independent copies of application components, including data stores.
	Event Sourcing					Use an append-only store to record a full series of events that describe actions taken on data in a domain.
	External Configuration Store	Move configuration information out of an application deployment package to a centralized location.
	Failover 						Switches to a backup system/component when the primary one fails, which ensures continuity of service by having redundant systems ready to take over
	Federated Identity				Delegate authentication to an external identity provider.
	Gateway Aggregation				Use a gateway to aggregate multiple requests into a single request.
	Gateway Offloading				Offload shared/specialized service functionality to a gateway proxy.
	Gateway Routing					Route requests to multiple services by using a single endpoint.
	Geode							Deploy back-end services across geographically distributed nodes. Each node can handle client requests from any region.
	Health Endpoint Monitoring		Implement functional checks in an application that external tools can access through exposed endpoints at regular intervals.
	Index Table						Create indexes over the fields in data stores that queries frequently reference.
	Leader Election					Coordinate actions in a distributed application by electing one instance as the leader. The leader manages a collection of collaborating task instances.
	Materialized View				Generate pre-populated views over the data in data stores when the data is poorly formatted for required query operations.
	Messaging Bridge				Build an intermediary to enable communication between messaging systems that are otherwise incompatible.
	Pipes and Filters				Break down a task that performs complex processing into a series of separate elements that can be reused.
	Polyglot Persistence			Uses multiple database technologies to optimize for different data models, access patterns, and scalability requirements
	Priority Queue					Prioritize requests sent to services so that requests with a higher priority are processed more quickly.
	Publisher/Subscriber			Enable an application to announce events to multiple consumers asynchronously, without coupling senders to receivers.
	Quarantine						Ensure that external assets meet a team-agreed quality level before the workload consumes them.
	Queue-Based Load Leveling		Use a queue that creates a buffer between a task and a service to smooth intermittent heavy loads.
	Rate Limiting					Avoid or minimize throttling errors by controlling the consumption of resources.
	Retry							Enable applications to handle anticipated temporary failures by automatically retrying failed operations bc of transient errors, typically with exponential backoff
	Saga							Manage data consistency across microservices in distributed transaction scenarios (saga choreography and saga orchestration)
									The saga orchestration pattern uses a central coordinator (orchestrator) to help preserve data integrity in distributed transactions that span multiple services
									The saga choreography pattern helps preserve data integrity in distributed transactions that span multiple services by using event subscriptions
									In a distributed transaction, multiple services can be called before a transaction is completed. 
									When the services store data in different data stores, it can be challenging to maintain data consistency across these data stores
	Scatter-gather					A message routing pattern that broadcasts similar/related requests to multiple recipients, and aggregates their responses back into a single message by using an aggregator component
	Scheduler Agent Supervisor		Coordinate a set of actions across distributed services and resources.
	Sequential Convoy				Process a set of related messages in a defined order without blocking other message groups.
	Sharding						Divide a data store into a set of horizontal partitions or shards.
	Sidecar							Deploy components into a separate process/container to provide isolation and encapsulation.
	Static Content Hosting			Deploy static content to a cloud-based storage service for direct client delivery.
	Strangler Fig					Incrementally migrate a legacy system by gradually replacing pieces of functionality with new applications and services.
	Throttling						Control the consumption of resources from applications, tenants, or services.
	Transactional Outbox			The outbox table resolves the dual write operations issue that occurs when a single operation involves a database write operation and an event notification which can create inconsistencies if one fails
	Valet Key						Use a token/key to provide clients with restricted, direct access to a specific resource or service.

	- distributed system architectures:
		- client-server architecture: servers provide resources and clients request them, communicating over a network
		- peer-to-peer architecture (P2P): each peer/node in the network acts as both a client and server, sharing resources directly with each other
		- three-tier architecture: has presentation (UI), application (business logic), and data (database) layers, where layers are separated to allow scaling and maintenance
		- microservices architecture: the application is split into small independent services which handle specific functions, where these services communicate over a network often using REST APIs or messaging
		- service-oriented architecture (SOA): similar to microservices, SOA organizes functions as services but SOA typically uses an enterprise service bus (ESB) to manage communication between services
		- event-driven architecture (EDA): components interact by sending and responding to events rather than direct requests, where an event triggers specific actions or processes in various parts of the system

- kubernetes
	- master node
		- API server: front end and communication center, coordinates cluster operations
		- scheduler: assigns pods to nodes based on resource requirements and availability
		- controller-manager: handles worker failures, tracks workers, performs cluster functions like replication
		- etcd: key-value database to store cluster data like scheduling info, pods, state info, etc
	- worker node
		- kubelet: reads container manifests to check container state and ensure pods are functional
		- kube-proxy: manages network rules to allow connections to pods, handles load balancing
		- container runtime (docker/containerd): runs containers

- sources
	https://igotanoffer.com/en/advice/amazon-system-design-interview
	https://www.geeksforgeeks.org/system-design/amazon-system-design-interview-questions/#
	https://www.geeksforgeeks.org/python/python-design-patterns/
	https://learn.microsoft.com/en-us/azure/architecture/patterns/
	https://www.geeksforgeeks.org/cloud-computing/kubectl-cheatsheet/