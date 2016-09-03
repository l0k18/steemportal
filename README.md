# steemportal

https://github.com/l0k1-smirenski/steemportal

A python3 application for accessing and interacting with the Steem blockchain forum system. It uses Piston, from the user @xeroc, whose main page can be found here: http://piston.readthedocs.io/en/stable/ It also uses code from a port from the project 'mdpreview' which you can find here: https://github.com/fboender/mdpreview which is used to enable markdown previewing.

The app is being written with a modular interface glue to select between interface frontends. The default will be Gtk3/GLib2. I invite other developers to write the other front ends - the modularised intermediate code is not written yet but once it is, the frontends will be able to link to the core.

Apologies for the messy filesystem as this modularised architecture is put into place.

### Motivations for this project

#### Web Browsers are Slow and Inefficient

This project is just beginning and I am going to spend a lot of time working
on it while I have the opportunity. There is a lot of work being done on the
Steem blockchain system, but the main official web portal's web interface is
heavy and slow especially with long comment threads.

#### Personalised Blocking of Posts by Users

There is also absolutely no mechanism aside from when a user gets flagged so
much they end up with zero or lower reputation score, they disappear from
the comment feed. The 'mute' mechanism does nothing but really highlight who
you muted, just as pixellation, blurring, black boxes, beeps and silence in
offensive content censorship systems actually draw attention to the supposed
offensive material. Obviously this small thing may be eventually fixed on
the steemit.com website.

#### Topic and Social Grouping

The above two goals are primary, but after these are added and functional,
I will be implementing a simple, small permissioned blockchain system
similar to Namecoin, except also with group membership moderation, and a
mechanism based on secret shares to allow delegation similar to a board.
https://en.wikipedia.org/wiki/Secret_sharing This blockchain will run as
part of this application, but there is no reason why it cannot be
stand-alone, although being so small there is no real reason for it to not
be simply integrated into viewer applications.

This system will allow you to filter posts according to the posters'
membership in the group, group administrators will be able to include and
exclude individual users based on their behaviour. It effectively should
enable multiple level hierarchic 'page management' functions as well. The
main goal, however, is to help group by subject and affinity, which will
become more important the bigger the Steem community gets.

There is moves afoot to create a groups system within Steem itself, and this will be integrated once it rolls out.

#### Messaging and Email

By integrating a headless bitmessage server into an installation, steemportal will be able to send messages between users seamlessly. By sending a tiny transfer to a user, a memo provides the corresponding bitmessage address, and steemportal will recognise this and add the user->bitmessage correspondence as a contact invite. Then the interface will, for confirmation, return the amount sent with a memo containing the bitmessage address for the return messaging. I have to look into it but I believe that the public key for Steem accounts can be used for encrypting messages, so if possible, these memos will be thusly encrypted. Then there will be a message reading interface, and it will also use markdown just like in posts, except no media is loaded, URLs are shown instead, naked and stripped, in case this is some attempt to locate someone's physical location, any oddities in the URL can be seen.

By taking the code of Bitmessage, but lowering the PoW requirement by 1/10th or maybe a little more (perhaps 1/100th), shortening the TTL expiry duration to a few hours, and a message size limit, perhaps something like 512 characters, there is also another serverless network system that searches for peers in a DHT node database, that sends much shorter, more frequent messages in the same way as Bitmessage - by simply propagating them, always encrypted to the secret key of the address. With a shorter PoW this should happen within a few seconds, while retaining the advantage that the receiver's location is not revealed by traffic patterns.

When the group message system is up and running, the messages, both email and instant messages, will send to a group's address, who then encrypts them to all the valid current members. Prior to that feature existing, the messaging system will be entirely based on Bitmessage functions. Open, unmoderated groups can be formed by the use of broadcast/subscription addresses. Of course this would likely get a bit messy after a while but user ID's are all linked and the email and chat systems would likewise not picku up messages from blacklisted users. A user can potentially be able to message all of their followers at once, for example. Nodes will also be able to query each other to build up username/BM/IM databases, so finding other users will be simplified.

### Installation

These instructions are somewhat outdated, the mechanism for isolating backend and frontend is being revamped. Watch this space.

You must have python3 and install python3-pip, and then with these two pre-
requisites, you can then install piston using:

> pip3 install steem-piston [--user]

Then, to run whatever has been written so far, you just run:

> python3 steemportal.py

I am still working on other elements. It uses the dconf registry system to
store credentials and settings in an instantaneously active manner, and to
persist sessions between launch, so there is a script to install the schema:

> sh install_compile_schema.sh

This adds a configuration branch you can see
if you open dconf-editor and look for org->ascension. It may be already
executable, I am not sure if git preserves executable file attribute bits,
if they are, you can do this instead:

> ./install_compile_schemas.sh

I advise also for you to set the default RPC endpoint in piston thusly:

> piston set node wss://node.steem.ws

This changes the default endpoint from this.piston.rocks to the
load balanced clusters that are anycast-style nearest of several to
where your point-of-presence is.

Of course, use whichever editor or IDE you want if you wish to edit the
python scripts in this repository, but I recommend Geany, and because the
configuration file is in the repository, it will automatically set tab
sizes and the use of spaces to match the rest of the file.

Ultimately, this application will also contain the option to run both a Steem witness node and will be running the BM and IM (modified bitmessage for instant message chat) by default. With this full configuration if outbound connections are made through a Tor proxy or so, there would never be identifiable links between senders and such a node as to user to IP address correspondence. The chat systems originate messages but without full 100% access to the network, knowing for certain whether a node originates a message or not is very difficult to determine, and the message blocks in these messaging systems propagate and are cached by other nodes for the TTL duration, and then are flushed from the cache. 

Who actually picks it up cannot be determined. With the use of a local Witness node, one's traffic simply looks the same as any other Steem node, simply receiving and certifying received new blocks. So if it is also built in as an option, to use Tor or other, to send new transactions out, the location of such a node is protected from correlation attacks.

### Copyright, or lack thereof

I claim no copyright on this work, nor do I, by doing so, permit the
redistribution of it without this lack of copyright. Only because if you do,
you will get flagged for plagiarism and it certainly won't have record of
prior art. Not that I think it's going to be anything special, but you can
do whatever you like with it, but unless you change it substantially, you
simply can't claim it is your work.
