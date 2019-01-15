# SIP-VoIP-call-implementations-in-Linux-OS-

The aim of the project is to understand the implementation of SIP [Session Initiation Protocol] to enable media transfer or voice communication. The project comprises of one server and three clients to implement the four phases. The server software used is Asterisk Software and the clients use X-Lite soft phones to implement voice calls. Client registers with the server and calls are then established. Four different call scenarios are observed and implemented. The call scenario packets are screen captured using Wireshark and call flows are also observed.

This particular report contains the virtual machine approach, and not the ad hoc approach.

## Call Scenarios:

1. Call between two sip clients

-  Two SIP clients are configured on the two laptops and how they register with the Asterisk server and also how a call will be made between them via the server.

2. Busy User
3. Call on Hold
4. Conference Call
