# Development Roadmap for steemportal

To help guide other contributors, should they decide to join the
development of this project, I am laying out the sequence of development
that I think this project should follow

## Read Only Interface

First step is to create a view-only implementation of the interface.
The various elements need to be created, a basic URL navigation log for
forward and back, and interfaces that pop up dialogs for interacting
with the wallet and account configurations.

In keeping with the Gnome 3 Human Interface Guidelines, I aim to make
this app entirely in keeping with the interface style and mechanisms
that people will be familiar with from using other Gnome 3 apps.

When for example a user is in the middle of composing a new post, the
composition buffer should be persisted as a series of periodic CVS type
annotation codes so that even after the app is shut down, they can undo
and redo their edits as they go, and in the menu it will be possible to
find un-committed new posts that can be continued or discarded.

To optimise performance, the lightest possible interface methods will
be used to render the display. Rather than a full HTML renderer, a
simpler markdown renderer will be used.

There will also be a user-customisable blocklist that will be queried
to determine if a post or comment should be displayed on the interface.
This was a major motivation in the first place for beginning development
on this application.

## Write Functions

The foregoing read-only interface should be completed before any write
functions are implemented. This helps also reduce errors for developers
as they test the interface with their own accounts. The version number
will remain as 0.1 until the full read only interface is finished, and
only amended to 0.2 when a complete working set of full write functions
are added, including post creation, voting, wallet transfers, buy and
sell, and so on.

## Analytic functions

Once a complete working read and write interface is done, then analytic
functions will be created. The read interface already includes totals
like post count, and wallet transfer logs, but more indepth functions
will come later, and when this phase of development begins, we will
bump the version number to 0.3.

## Advanced functionality

The option to further improve the interface, such as a WYSIWYG editing
interface, will come during this 0.3 phase of development also. There is
other features planned as well.

One of the advanced functions planned is the creation of a peer to peer
group management system, which I am calling SteemHordes. This is
basically a kind of name space blockchain, including a delegation
mechanism for group founders that uses shared secrets to require
x of y delegates to sign a founder-level action within a specified time
period.

### Groups

This feature is going to be available from the core, so it will be integrated when it becomes available.

The other advanced function planned is based on the SteemHordes group
system, which will be a distributed chat system. This will initially
only implement public chatrooms, but it will work using a lightweight
protocol similar to Bitmessage to distribute the chatter in the network.
To decrease latency, it will prioritise its selection of peers as it
locates them, of users who are also part of the same chat. Unlike
Bitmessage, the objective is not to secure an email system, but rather
to enable a serverless chat system that ties in with the groups.

After the public viewable side of the chat is created, the chat system
will implement an encryption system, which also respects users blocks
of unliked other users that may be within the same group, by not
encrypting to their keys, implementing cryptographically the bilateral
direction of blocking through cryptography, for users in chatrooms that
the founders wish to be encrypted.

There will of course also be direct messaging, and this will be
implemented after the foregoing, because it will be encrypted by
default.

When a chatroom is marked as private, and requires encryption, users
clients will also not advertise their location, or, this can be an
additional mode. This eliminates the possibility of discovering which
nodes have which user connected to them.

### Email and Instant Messaging

By building an announce channel for this chat system, users can propagate contact details, and nodes will log these into a database of steem username, steem public key, Bitmessage address and Instantmessage (The higher speed, lower message size limit bitmessage-like instant messaging system), and each node will thus be able to cache a full directory of users and keys. Nodes will advertise these, as well as updates, and for security they are signed messages so it can be proven the keys are controlled by the user claiming this ability. The same system as used by bitmessage for broadcast/subscriptions for open mail and chat propagation. When groups are created, the propagated messages for the groups will be sent out encrypted for the currently listed members. If bogus messages are received that come from non-members of a group, they will be dropped.
