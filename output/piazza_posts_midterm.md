
6.033 Piazza Posts
==================


This file includes all piazza posts scraped as of noon 3/31. Only instructor and student answers have been included. 
Followup discussion was omitted to keep things short and sweet.
# @679 DCTCP vs. TCP with RED/ECN
- Question: What is the difference between DCTCP and TCP with RED/ECN?
- Tags: exam1
- Students' Answer: 
- Instructors'
 Answer: 
# @678 2017 Q13 TCP
- Question: What does TCP do for clients A, B, and C? Can someone walk me through it? I saw the other piazza post on 
this question but I don’t see how the queue will always be at a length below 10 packets, since 1 packet is being sent to
 destination D and 3 are being sent into the queue every time  Edit: It makes sense if D is sending ACKs to clients A, 
B, and C, but why is the queue not sending ACKs for packets added to it?
- Tags: exam1
- Students' Answer: 
- 
Instructors' Answer: 
# @677 RON node at destination
- Question: This is a follow-up to @656. Suppose there are three nodes A, B, and C such that A knows about a path to B 
and B knows about a path to C but A does not know a path to C. If there are RON nodes at A and B, then is A able to send
 anything to C? My impression from reading the RON paper was that the answer is no, since RON nodes only communicate to 
each other about paths to other RON nodes – in order for the RON node at B to know about the path to C, the RON node at 
B would have to be sending probes to arbitrary other nodes in the network, which doesn't seem to be indicated by the RON
 paper.However, the answer key to 2018 Q8 (as well as the video explanation and the Piazza answer to e.g. @656) seem to 
indicate that A can still send traffic to C (but not receive anything back). How is this possible?
- Tags: exam1
- 
Students' Answer: 
- Instructors' Answer: I’m assuming here that you meant 2019 Q8: First the case where we just have 
RON nodes at XA and B: XA knows a path to B, and B knows a path to XC, so we can get from XA to XC. RON nodes know about
 the normal BGP paths for these segments, so that is how it is sent. However, in the other direction, XC only knows how 
to get to B, and no farther, so it will not send traffic to there in hopes of getting to XA, because it doesn’t know 
that B and XA are connected via RON, since it is not a RON node itself. Now the case where we have all 3 RON nodes: XC 
will know the path to B, and B knows the path to XA. What is new here is that XC knows the full path to XA that it can 
use through B since it is now part of the overlay as well. Does that make sense?
# @676 2018 Q14
- Question: It makes sense that for b and d, we read 1 packet/queue/round, and this isn’t true for a or c. But how does 
this relate to the two-second window constraint that the question puts on us, and why does it matter that we only send a
 single packet/round? Thank you!
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: 
# @673 2018 Question 10 A and 10 B
- Question: In the answer key shouldn't 10A and 10B be flipped? I thought that link state was the global Dijkstra one 
and Distance Vector was the greedy one.
- Tags: exam1
- Students' Answer: Unsure what you mean by global but the way to 
solve this is to know the content of the advertisements. Link state stores the link costs. Distance vector stores path 
costs.
- Instructors' Answer: 
# @671 Course data for download
- Question: I've downloaded all the course files (lecture slides, recitation readings, outlines) for exam 1 and uploaded
 them to Google Drive: https://drive.google.com/drive/folders/1ONq16mP0TI3d3blmFs4lKWWCytqqGkrj?usp=sharing(This doesn't
 include the textbook, since that is not legally available for free download)
- Tags: exam1
- Students' Answer: 
- 
Instructors' Answer: 
# @670 2019 6C-c
- Question: What is INFINITY generally set to?
- Tags: exam1
- Students' Answer: A small-ish integer number.
- 
Instructors' Answer: 
# @669 Ethernet
- Question: I think I'm a little bit confused about how Ethernet works. Can multiple packets be sent on the Ethernet at 
the same time (as long as they are far enough apart)? Based on 2019 5A, it seems like multiple packets could be sent in 
a single RTT, but I thought that multiple packets couldn't be sent without causing a collision.  Thanks!
- Tags: lecture

- Students' Answer: 
- Instructors' Answer: 5A is saying that a collision will occur if two stations send signals at 
roughly the same time. Packets can be sent at the same time, but will collide since their signals interfere. Does this 
help?
# @668 2018 Q8
- Question: Why is it that (b) is not sufficient – why do we need an additional RON node? Can’t seem to get why.
- Tags:
 exam1
- Students' Answer: L won’t advertise its path to C to K since only customers are advertised to peers.
- 
Instructors' Answer: 
# @667 Spring 2017 14B
- Question: In the problem statement, it’s mentioned that T1T_1 treats packet marks the same way it would treat drops. 
Given that T1T_1 experiences 4 marks (and is presumably using AIMD) why doesn’t it’s window decrease by 1/16 instead of 
1/2 as mentioned in the answer.
- Tags: exam1
- Students' Answer: In AIMD, W is only updated once every RTT and not 
after each drop.
- Instructors' Answer: 
# @666 Is there OH tomorrow afternoon?
- Question: ^
- Tags: logistics
- Students' Answer: 
- Instructors' Answer: 
# @665 Distance Vector Routing
- Question: How does distance vector routing deal with failed links (assuming timing works out so that costs don’t go 
into infinity) alongside trying to find the smallest cost? How does it update the weights to a higher cost (in the case 
of failure or longer delays in topology) when it is meant to minimize each cost and would theoretically ignore these 
higher costs?
- Tags: lecture
- Students' Answer: 
- Instructors' Answer: In the attached textbook readings (chapter 18 
specifically), two strategies are discussed. The key insight to these approaches not working out is that we need some 
sense of global state (i.e the entire path) to determine how to deal with failures. With the entire path given, then it 
is possible to rule out situations of inconsistent state that can cause the count to infinity problem. This is what path
 vector routing does. Of course, there is a trade off due to the additional overhead of storing the path. 
# @664 Partial credit?
- Question: Is there partial credit on the exam for multiple choice and T/F questions if we show our work?  Is there 
partial credit generally?
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: There will be partial credit, but 
usually T/F questions don't usually have many opportunities for partial credit
# @663 Spring 2014 6C
- Question: http://web.mit.edu/6.033/2016/wwwdocs/assignments/old_quizzes/s14_1.pdfp. 8 6CWhy is this false?An argument 
for true: DCTCP has high throughput generally right? According to the paper it delivers "same or better throughput than 
TCP".An argument for false: DCTCP is sending less stuff, so TCP just takes advantage of DCTCP's preemptive reduction of 
sending to send more stuff?How to tell that one argument is better than the other?
- Tags: exam1
- Students' Answer: 
- 
Instructors' Answer: 
# @662 TCP vs DCTCP reaction to congestion
- Question: In one question I found from previous years it says that DCTCP reacts to congestions faster than TCP. Why is
 that true? I think about DCTCP as kind of adaptive and therefore slower to change the size of the window of its 
senders, whereas TCP just divides by half all the time. DCTCP may be better but TCP is more aggressive and therefore 
handles congestion much faster, no?
- Tags: exam1
- Students' Answer: TCP responds when stuff is being dropped, or it 
isn't getting ACKs back.  DCTCP responds when your queue size is not great, which is earlier than a problem already 
happening with your queues being too full.
- Instructors' Answer: 
# @660 Questions about VMM
- Question: How does trap and emulate work? And what's binary translation in VMM?
- Tags: lecture
- Students' Answer: 
Trap and emulate basically means whenever VMM wants to do something on behalf of the guest OS because the guest OS 
thinks it is its own machine, the guest OS needs to make an exception so that VMM can trap that exception, then 
"emulate" i.e. do whatever is needed to make the real changes to the system that the guest OS wants but doesn't have 
access to.  From the lecture outline on this:  "Binary translation: VMM analyzes code from guest OS and replaces 
problematic instructions"
- Instructors' Answer: 
# @659 Stack Corruption
- Question: What is stack corruption when we talk about threads in lec 05?
- Tags: lecture
- Students' Answer: 
- 
Instructors' Answer: Stack corruption is when memory locations on the stack are improperly accessed. This can occur due 
to the release and require of the lock in the code on page 15 of the abbreviated animation slides for the lecture
# @656 RON
- Question: In order for RON to work, do the starting and ending nodes both need to be RON (or is it possible for data 
to still be rerouted by an intermediate RON need even if the starting/ending node isn't RON)?  Thanks!
- Tags: 
recitation
- Students' Answer: 
- Instructors' Answer: 
# @655 Textbook Solutions
- Question: Are there solutions to the textbook questions (questions at the end of each chapter) posted anywhere? 
Thanks!
- Tags: other
- Students' Answer: 
- Instructors' Answer: Not that I'm aware of, sadly!
# @654 2018 #3
- Question: For the guest virtual page 3, why would we set W to 0 and U to 1 instead of the other way around (W to 1 and
 U to 0)? Wouldn't the VMM need to take control whenever the page table is accessed (to translate it into a physical 
address)?  Thanks!
- Tags: exam1
- Students' Answer: The VMM isn't a kernel really so it doesn't take control as far as 
I know (like it's not handling exceptions in the usual sense I think).  The reason why W = 0 because notice that Guest 
OS page table is in guest-physical page 4. For VMM to know about writes to the page table guest OS changes need to 
trigger an exception, and making the page table read-only (W = 0) does this.  The reason why U = 1 is because from the 
standpoint of the outside world, guest OS is always a user (even if it thinks its K bit is 1 relative to everything 
else) so the U bit relative to the outside world needs to be set to 1 for the guest OS to use it at all.
- Instructors' 
Answer: 
# @652 2019 4C
- Question: Why is the value of p 12 and not 10? To my understanding, a single page is 4096 bytes with each entry in the
 page being 32 bits. Doesn’t this mean that there are 2102^{10} entries instead in the page table?
- Tags: exam1
- 
Students' Answer: I had the same mistake. 4096 is the size of the page (the actual data), that's the number of offsets 
you can fit. So, there are 12 offset bits, for 2^12 spots.The 4 byte thing is talking about entries in the page table, 
not the entries in the page itself.
- Instructors' Answer: 
# @651 2017 Q9
- Question: 1) From the RON paper, routing decisions are made from knowledge/metrics about the network. In this question
 though, we don't get additional metrics so what kinds of behavior changes does laying down a RON node actually entail? 
Is it just additional visibility between RON nodes?  2) To check my understanding, would it be true that: - If we added 
RON nodes in A and B instead, the desired route would be taken - If we added RON nodes in B and C instead, the desired 
route would not be taken because B still does not advertise to A its peer path.  Thanks!
- Tags: exam1
- Students' 
Answer: 
- Instructors' Answer: 
# @650 2017 Q7
- Question: From Step 1, C has cached the address for www.a.com provided by the name server responsible for a.com  How 
does this help with step 4, where C seems to also have the address for a.com cached? Though www.a.com and a.com are 
related, wouldn't they be two separate IP addresses, with only the former cached?
- Tags: exam1
- Students' Answer: 
- 
Instructors' Answer: @549 for a detailed explanation  the referral records (who is responsible for what) are cached so 
that's why we see performance boosts.  But see the linked post for a much more detailed explanation
# @649 Spring 2015 2
- Question: http://web.mit.edu/6.033/2016/wwwdocs/assignments/old_quizzes/s14_1.pdf  p. 3  Do we assume the the default 
name server is operating recursively (therefore it can query .edu and give it to the client?)  Could you please explain 
the answer? How can both B and C be correct?
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: I think this is a
 fair assumption given the answer choices. A recursive server might have the records from either B or C cached if it has
 answered related queries before.
# @648 Spring 2017 Q11
- Question: For slow start, we just need exponential growth, right? It doesn’t need to specifically double every time, 
but for each unit increase of RTT, our window size must be multiplied by a number &gt; 1?
- Tags: exam1
- Students' 
Answer: 
- Instructors' Answer: Slow start is defined as doubling. More specifically, it works like this: every time the
 sender receives an ACK, it increases its window size by 1.  That might look like linear growth, but here's what 
happens: * Sender sends one packet; gets one ack; increases W to 2 * Sender sends W=2 packets (one full window); gets 
two ACKs; increases W to 4 (W + 1 + 1) * Sender sends W=4 packets (one full window); gets four ACKs; increases W to 8 * 
etc.  So we see a doubling roughly every one round-trip-time.
# @647 2017 Q10
- Question: Are we assuming that the sender is continuously sending packets? If not, then other answers are correct.  
For example in B, The sender didn't send anything after sending 104.&nbsp; After receiving two 104 sacks. All future 104
 acks get dropped until the sender transmits 105. The receiver receives 105, and sends acks for it but it gets delayed 
or dropped. The sender sends 106.&nbsp; The receiver receives 106, and starts sending 106 ack.&nbsp; The connection 
continues working normally.
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: 
# @646 Office hours today
- Question: Looks like the queue is disabled for office hours today at 4.
- Tags: exam1
- Students' Answer: 
- 
Instructors' Answer: 
# @645 Are there virtual OH right now?
- Question: I thought there were office hours today from 4-5 but I'm not able to join the queue, is there somewhere else
 I should be looking to join the OH?
- Tags: logistics
- Students' Answer: 
- Instructors' Answer: 
# @644 Clarification on slow-start in TCP
- Question: I found it confusing how slow-start is defined in the lecture slides and would just like to confirm that 
slow-start in TCP is when the window size is increased by 1 for each ACK received whereas an optimization to combat 
slow-start is to instead double the window size every RTT. Also, in general, is slow-start an undesirable mechanism of 
TCP (i.e. we would want to make the above optimization to improve performance in most cases)? Thanks!
- Tags: exam1
- 
Students' Answer: 
- Instructors' Answer: Check out @648. The two approaches you've suggested -- increasing the window 
size by one for each ACK and doubling the window size every RTT -- are actually essentially the same.  Slow-start is not
 an undesirable mechanism. We want it at the beginning so that connections can quickly ramp up from a window size of 1 
to the full window size. This is especially impactful for connections that don't last very long.
# @643 Spring 2017 Q9
- Question: I wanted to ask an additional question about the BGP relationships in this graph:  For the customer x on the
 bottom, I believe that x knows about A, B, y, and T1, but since T1 is peers with T2 and T3, would x also know about the
 providers T2 and T3? Or would it still only know about T1?&nbsp;
- Tags: exam1
- Students' Answer: 
- Instructors' 
Answer: 
# @641 Eraser Question
- Question: On page 19, the paper says "the violation of the locking discipline will be reported only if the write 
precedes the read" when discussing a possible modification to the lockset algorithm that accounts for multiple 
protecting locks. In the example given, I was wondering how the violation would *ever* be reported with the modified 
algorithm, since presumably C(v)C(v) will become the set {m2}\{ m_2 \} and thus not empty.
- Tags: exam1
- Students' 
Answer: 
- Instructors' Answer: 
# @640 Network questions
- Question: CDN and P2P support communications are at which level of architecture? Is it application, transport, 
network, or link? When we talk about how ethernet supports communication between two directly-connected nodes, what do 
we mean by nodes? Are they different computers/ devices?
- Tags: lecture
- Students' Answer: 
- Instructors' Answer: We 
typically think of CDNs and P2Ps as operating at the application layer. CDNs will do some transport-layer tricks -- for 
instance, Akamai does some smart things with TCP to improve performance -- but they are application-layer things.  Nodes
 typically mean two different machines (could be computers, could be switches).
# @639 2018 Q3 guest OS in U vs K mode?
- Question: p. 3  http://web.mit.edu/6.033/www/assignments/old_quizzes/s18_1.pdf&nbsp;  I have heard the bits in the 
rightmost column in the box should be 0 if the guest OS itself is in user mode (relative to itself) and 1 
otherwise.&nbsp;  However, I have also heard that those bits should always be 1, because the guest OS will block itself 
from accessing kernel only pages (relative to itself) in its own page table, so it's not needed to enforce this in the 
shadow table.  Could you please clarify which answer is correct?
- Tags: exam1
- Students' Answer: 
- Instructors' 
Answer: resolved
# @638 2018 8
- Question: http://web.mit.edu/6.033/www/assignments/old_quizzes/s18_1.pdf  p. 7&nbsp;  If C wasn't a RON node would 
this answer still work?
- Tags: exam1
- Students' Answer: @656
- Instructors' Answer: 
# @637 Spring 2017 question 9
- Question: I’m having some trouble determining the default BGP path in this situation. I thought the precedence in 
routing would be customers, peers, and then providers (so x -&gt; A -&gt; B -&gt; C -&gt; z) Any clarification on that 
(and why choice c is correct) would be greatly appreciated. thanks!
- Tags: exam1
- Students' Answer: 
- Instructors' 
Answer: Similar answer to @610. B does not tell A that it has a peering relationship with C, and will not send A’s 
traffic to C, so the (x -> A -> B -> C -> z) path is not one that exists as far as x knows. T1 peers directly with T3, 
so the only path we have available before RON nodes added is (x -> A -> T1 -> T3 -> C -> z). Choice c is correct because
 only when we also have a RON node at all of A, B, and C, do we know about the path (x -> A -> B -> C -> z) and can use 
it.
# @636 2019 6A Link-state routing
- Question: Why is the total advertisement 2 * link * node? This is not obvious for me.&nbsp;
- Tags: exam1
- Students' 
Answer: 
- Instructors' Answer: Think about one node (let's call it A). A sends advertisements to all of its neighbors, 
which immediately forward them to all of their neighbors, who forward them to all of their neighbors, etc. It's 
difficult to think about how many total that advertisements that would be if you only focus on the number of nodes. But 
think about how many advertisements travel across a link: it's always two -- one from each endpoint. So for a single 
node's advertisement, we see 2L copies. (You can see this happen in the animations of the link-state slides in lecture)
  Then, if we care about all N nodes, we have 2L copies of each node's advertisement. So 2LN.
# @635 2019 4D
- Question: The answer is (2^m + 2^(m+n))*4 Bytes. As for how I understand it, this means that the first-order page 
stores 2^m addresses, and the second-order pages stores 2^(m+n) addresses. However, in order for us to use all the 
potential 2^(m+n) addresses by the second-order page, doesn't each entry in the first-order page point to a second-order
 page instead of an actual address? Why do we add them together? I thought it would be an either-or relationship.&nbsp;

- Tags: exam1
- Students' Answer: One of the 2^m is for the top level page table.  Then, you have one lower level page 
table of size 2^n for every single of the 2^m entries of the top level page table.  So, the total usage is   4 bytes per
 entry (2^m entries in the top level page table + (2^m)(2^n) entries across all of the bottom level page tables)
- 
Instructors' Answer: 
# @633 2019, problem 5B
- Question: This problem states that Ethernet receivers do not send ACKs upon receipt of a packet that passes a CRC 
check, but my question is do the higher layers like the application layer send back acknowledgements, and if not, how 
does the sender know that the packet was successfully received? Thanks!
- Tags: exam1
- Students' Answer: 
- 
Instructors' Answer: 
# @631 Link-State Routing
- Question: Are the ads the direct costs to the other nodes or are the ads the known shortest costs? So in the lecture 
example, does A keep sending the same ad as long as its neighbors are alive, or does it start sending ads including 
information about other nodes once it learns about them?
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: Link-
state advertisements reflect a node's link costs to its neighbors (which may not be the shortest paths to its 
neighbors). A node's link-state advertisement would change in the case of failure, but also if the costs to any of its 
neighbors changed.
# @629 2014 #15
- Question: Why wouldn't AS3 and AS6 send traffic to AS4? Thanks!
- Tags: exam1
- Students' Answer: AS3 can reach MIT 
through AS5 which is a customer, so that route is preferred over AS4, which is a peer. Similarly AS5 is a peer for AS6 
while AS4 is a provider.
- Instructors' Answer: 
# @628 2014 #13
- Question: Why would the path be AS4 → AS3 → AS5 → MIT? Why would AS2 advertise their provider to AS4? Why wouldn't the
 correct path be AS4 → AS1 → AS2 → MIT?  Thanks!
- Tags: exam1
- Students' Answer: The default import policy is to 
prefer customers over peers over providers, so AS4 prefers AS3 over AS1.
- Instructors' Answer: 
# @627 2019 Spring 2019
- Question: http://web.mit.edu/6.033/www/assignments/old_quizzes/s19_1.pdf  p. 7. 5B(d), I thought that failed 
transceivers drop out of the Ethernet before they can do damage to the system. COuld you please explain why this is/give
 an example of a transceiver breaking the segment, and/or point me to the right passage?
- Tags: exam1
- Students' 
Answer: Transceivers are designed such that common failures such as loss of power don’t interfere with the rest of the 
Ether. However, other types of failures, such as a transceiver continuously transmitting random bits, would prevent the 
rest of the system from functioning.
- Instructors' Answer: 
# @626 Spring 2018 Q14
- Question: Why is D correct? Wouldn’t the norm for both be 1/30 since norm = weight / mean packet size and Q1 would be 
1/30 and Q2 would be 2/60 ?
- Tags: exam1
- Students' Answer: The norm for both is 1/30 so n_packets will be 1 for both.
 Then in each round, one packet will be sent from each queue, which satisfies both requirements.
- Instructors' Answer: 
# @625 Multi-path routing and load balancing
- Question: Resolved. 
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: marking as resolved
# @624 2019 P4C
- Question: For problem 4C, why don't we convert the number of bytes in a page to bits, i.e., why isn't the answer 14 = 
log(2^12*2^2)?  Do we only care about offsets into a page at the byte level?
- Tags: exam1
- Students' Answer: In both 
RISC-V and x86, memory is byte-addressable so each virtual address represents one byte.
- Instructors' Answer: 
# @623 2018 P8
- Question: I am a bit confused about how RON and BGP works:- in this problem set-up, why couldn't BGP send packets via 
path 2 already? - moreover, why is it sufficient to only have 3 RON nodes? What enables the RON node in L to forward the
 packet to C if L only knows about K and T?
- Tags: exam2
- Students' Answer: 
- Instructors' Answer: First question is 
answered by student below.  Second question is because RON traffic travels in the underlying network, so if the 
underlying path is the best one without another RON node, it'll still take that path
# @622 2018 2a
- Question: Why is this answer false? I understand that synonyms exist, but wouldn't they link a DNS name to another DNS
 name (not directly to the IP address)?  Thanks!
- Tags: exam1
- Students' Answer: There is nothing preventing two A 
records for different domains from pointing to the same IP address.
- Instructors' Answer: 
# @621 2018 15
- Question: Why CDN can tolerate individual machine failures? What if the origin fails?
- Tags: exam1
- Students' 
Answer: 
- Instructors' Answer: If the closest server fails, then the CDN request routing logic will divert the request 
to the next closest server once it detects the failure. If the server fails in the middle of a request then the client 
will time out or the user will reissue the request, causing the CDN to route it to the closest working server. When the 
closest server is alive and the routing logic believes it is working but the client can’t reach it due to a network 
issue on the client’s path,  typically the DNS response will have multiple servers and the client could try the other 
servers.   The basis of the concept of CDNs is that there is no single origin and the system is distributed. 
# @620 2018 #3
- Question: Can someone explain why the guest virtual page 4 write bit is 1, but the guest virtual page 3 write bit is 
0? Both are running on kernel in the guest OS, so shouldn't they both be 0 to trigger an exception?
- Tags: exam1
- 
Students' Answer: @575 @604 The write bit for guest virtual page 3 is 0 because it is special in that this is where the 
guest OS page table is stored.
- Instructors' Answer: 
# @619 CDN using DNS rewrites
- Question: In the 2018 practice exam problem 15, what does it mean for CDN to use DNS rewrites? Does this mean DNS 
requests are going through the edge-servers in a CDN, and if not how do I interpret this?
- Tags: exam1
- Students' 
Answer: See figure 5 and section 7.5.1 of the Akamai paper. A client will make a DNS request to one of Akamai’s DNS 
servers, which will return the address of one of its edge servers which will depend on the client’s location.
- 
Instructors' Answer: 
# @618 2017 Problem 3
- Question: I thought the reason the change causes deadlock is because no receiver can take a message out of the buffer 
while Zara holds bb.lock, so notify() will never trigger. The explanation in the solutions, however, mentions that 
wait() itself needs bb.lock. I was wondering why this is the case.
- Tags: exam1
- Students' Answer: 
- Instructors' 
Answer: I think this may mean the wait() needs the lock such that it can be released by this thread and the wait() of 
another thread (i.e. the receiver) can acquire the thread once woken up. The phrasing may be a bit confusing since the 
locks have been moved outside of wait() itself, but I think its the same principle. Does that help?
# @617 Why is P2P and Akamai an overlay?
- Question: And how do we recognize overlays?
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: 
# @616 2019 Question 9
- Question: Regarding question 9 on the practice 2019 exam, I'm a bit confused on a few parts: 1. What is the difference
 between a queue and a buffer? I can't seem to understand the difference between queue buildup and buffer pressure.  2. 
For part b of this problem, how exactly is time doubled for aggregation with this new change in structure? The video did
 not seem to explain it very clearly.
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: 
# @614 RON
- Question: How exactly does RON expose private links to other RON nodes? Does a RON node expose its private links to 
all the neighboring (possibly non-RON nodes), or does it only expose it to other RON nodes? If so, does that mean that 
RON nodes must be directly connected to other RON nodes, or can it send this information to all the RON nodes on the 
Internet?Sorry, I think I'm just quite confused about how these nodes work.  Thanks!
- Tags: recitation
- Students' 
Answer: My best guess for this is a RON node exposes what destinations it can reach to all other RON nodes, but a path 
between that node and whatever RON node wants to use its path needs to exist in the actual network itself. I'm not sure 
about the destination part of that but I think the end result is the same.  RON nodes don't have to be directly 
connected, but for RON node A to send to RON node B they need to be connected in the underlying network (this is called 
a virtual link in the paper I think).
- Instructors' Answer: 
# @613 BGP Question
- Question: Since BGP is an application layer protocol, how does it affect routing? Specifically, how does BGP tell the 
network layer which path to take? Thanks!
- Tags: lecture
- Students' Answer: 
- Instructors' Answer: BGP routers keep a
 routing table to know how to direct information. They establish and manage the local connection so they define the path
 already for TCP to run under it.
# @612 BGP
- Question: I just want to quickly clarify the relationships and communication in BGP. Is the following 
correct?Providers tell their customers about: themselves, their peers, their other customers, and their providers  
Providers tell their peers about: themselves and their customers (but not their providers or their other peers)  
Providers tell their providers about: themselves and their customers (but not their peers)
- Tags: lecture
- Students' 
Answer: 
- Instructors' Answer: Yes, this is correct!  Providers will tell their customers about everyone, but will only
 tell their peers and providers about their customers and themselves (in order to maximize profit).  
# @611 2017 Q13
- Question: A. I'm wondering how Change 3 improves the fairness of the protocol?  
- Tags: exam1
- Students' Answer: 
- 
Instructors' Answer: 
# @610 2017 Q8 peering confusion
- Question: Part A of this question: Why doesn't X know about Z or C when B and C have a peering relationship? Does this
 mean that A=B=C does not mean A=C? Moreover, why doesn't X know about T2 when A has a peering relationship with B? 
Thanks in advance!
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: From supplemental BGP reading: “The second 
prevalent form of inter-AS interconnection is called peering. Here, two ASes (typically ISPs) provide mutual access to a
 subset of each other’s routing tables. The subset of interest here is their own transit customers (and the ISPs own 
internal addresses”. So we can interpret this in the context of the question to mean that A and B’s peering relationship
 does not include access to C (and by extension z) because C is not actually a transit customer of B. Does that help? 
http://mit.edu/6.033/www/papers/InterdomainRouting.pdf
# @608 Spring 2018 Q4
- Question: If the line release(bb.lock) got moved to be after the bb.buff[my_send_index mod n] = m line, would this be 
a correct bounded buffer implementation?
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: Although, you would 
be avoiding a race condition on the following bb.buff[my_send_index mod n] = m line, there would be other issues to 
consider like deadlock situations which you can see in slide 39 of lecture 4
# @607 Lockset Algorithm
- Question: Does lock set algorithm only work with a single thread? I'm asking this because I thought data racing and 
deadlock only happen when we have multiple threads accessing the set of same variables.
- Tags: exam1
- Students' 
Answer: 
- Instructors' Answer: Eraser (and Lockset) work with multi-threaded programs! The pseudocode on page 6 of the 
paper would be executed for each thread I believe.
# @606 OH Today
- Question: We will be ending office hours an hour earlier just for today. We apologize for any inconvenience, and wish 
you the best of luck preparing for your exam!
- Tags: logistics
- Students' Answer: 
- Instructors' Answer: 
# @605 question on yield
- Question: What does yield, yield_wait, and wait do respectively?
- Tags: lecture
- Students' Answer: 
- Instructors' 
Answer: yield suspends the current thread and resumes another thread. wait tells us to suspend a thread and come back to
 it once a certain condition variable is true (via notify) yield_wait is a specific version of yield introduced in 
lecture that is compatible to be used inside wait (see http://mit.edu/6.033/www/lec/s05.pdf to see how the code differs)
# @604 2018 Problem 3
- Question: Why is it that the W bit for guest virtual 3 is 0 but the W bit for guest virtual 4 is 1? I don't see why 
the two W bits should be different since the last two rows in the Guest OS's page table have the exact same P/W/U bits?

- Tags: exam1
- Students' Answer: The guest page table is stored in guest virtual 3.
- Instructors' Answer: 
# @603 2019 3A
- Question: For 2019 3 A, can someone help give an example of the Lockset Algorithm when Eraser raises warnings?
- Tags:
 exam1
- Students' Answer: We call transfer(a, b) and then transfer(b, c). The first transfer will access the amounts 
for a and b while holding lock a, and the second transfer will access the amounts for b and c while holding lock b. 
Hence no lock protected the amount for b.
- Instructors' Answer: 
# @602 Link State Routing
- Question: Quick question, I'm wondering why the number of total advertisements sent with this would be about 2NL? 
Intuitively I would think it's NL since each node would send on the L links.
- Tags: lecture
- Students' Answer: 
Consider a single node
i
with
l
i
neighbors. For each of the
N
advertisements that it eventually gets, it will broadcast
 it to its
l
i
neighbors. Then the total number of advertisements will be
∑
N
i=1
N
l
i
=2NL
since each edge is counted 
in two of the
l
i
values.
- Instructors' Answer: 
# @601 Spring 2018 Problem 5
- Question: Why is d, "The value of x is changed for the last time before either foo() or bar() are called for the first
 time." a reason for Eraser not flagging the error? How does Eraser know that x will not be changed again? I know that 
in the Eraser paper, data races are not reported in the Shared or Exclusive state. However, we do not know if we are in 
these states because x could have been modified by multiple treads before foo or bar are called.
- Tags: exam1
- 
Students' Answer: The question is asking for reason that might explain a lack of Eraser errors in which case it is 
possible for
x
to be in an Exclusive or Shared state and it remains in that state for the remainder of the program. 
Because no writes are performed in foo() or bar() we know that the execution of either will not trigger a state 
transition to Shared-Modified and we can therefore assume that d is a valid possibility.
- Instructors' Answer: 
# @599 Thursday morning office hours this week
- Question: My office hours this Thursday will be 10:30am-11:30am instead of 11:00am-12:00pm.
- Tags: other
- Students' 
Answer: 
- Instructors' Answer: 
# @598 Links for Lectures 15 and 16
- Question: Lecture 15: https://mit.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=96f3a6c1-dbe0-4551-bb4e-ae6400d67fdb
 Lecture 16: https://mit.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=fa402b87-09c0-42fd-8124-ae6400d6ed66  Slides 
continue to be available on the website!
- Tags: lecture
- Students' Answer: 
- Instructors' Answer: 
# @597 Spring 2019 6B
- Question: I watched the video explanation for this problem but I'm still having some trouble understanding what is 
going through these timesteps at 26, 36, and 46. Could someone explain what is happening up to timestep 46 and how the 
E-F link failing impacts it?&nbsp;
- Tags: exam1
- Students' Answer: At 26, E knows that the cost 1 path to F no longer 
exists. At 33, C will advertise that it can reach F with cost 2, so E will now believe that it can reach F with cost 3 
by going through C (D will also do the same thing at 34). At 35, E will advertise that it can reach F with cost 3, so C 
now believes it can reach F with cost 4. At 43, C will advertise that it can reach F with cost 4, so E will believe that
 it can reach F with cost 5. This cost won’t be updated for the remaining timesteps up to 46.
- Instructors' Answer: 
# @596 Retransmition
- Question:  I am curious about what happens if there is a loss but there is no retransmition. If W is devide by 2, 
there must be loss of package, thus retransmit, but why only at this spot W goes back to 0? Is it true that all 
retransmit will lead W to be 0?
- Tags: recitation
- Students' Answer: 
- Instructors' Answer: So when there is a loss, 
there is always some type of retransmission. Sometimes that retransmission is handled by fast retransmit/fast recovery, 
other times by a timeout. Check out @565.
# @595 Lecture 6 Questions
- Question: 1. How exactly does the VMM intercept/trap an exception that occurs in a guest OS? How do we prevent the 
guest OS from trying to handle the exception itself?  2. How does having a special VMM mode make the VMM more powerful 
without having to modify the guest OSes?
- Tags: lecture
- Students' Answer: 
- Instructors' Answer: 
# @594 Certain Topics on Exam 1?
- Question: Are the following going to be tested on Exam 1? I saw questions about them on past exams (2017, 2018), but I
 don't remember them from recitation or lecture:  1. TDMA 2. Landmark Routing 3. MapReduce (though this was already 
answered by a student in @578, I just wanted to get confirmation)  If they were mentioned at some point, if someone 
could point me to where, that would be really appreciated!  Thanks!
- Tags: exam1
- Students' Answer: 
- Instructors' 
Answer: 
# @593 2018 Question 15
- Question: Can someone explain the differences bewteen CDN and P2P and why each is each for this question. Thank you 
-
 Tags: exam1
- Students' Answer: 
- Instructors' Answer: I think: a) both are overlays on top of existing internet 
network b) P2P can be pretty slow I believe compared to CDN’s which are designed for quick delivery of content c) see 
@619 d) p2p treats each peer equally, while CDN’s have a hierarchy of edge servers, parent servers, and origins e) if 
one peer goes down in p2p, we still have every other peer functioning. If a server in CDN’s, they have fault tolerance 
measures as described in the paper and many other servers that they can reroute traffic through
# @592 Eraser
- Question: If three threads seperately hold lock 1,2. for program 1, hold lock 1,3. for program 2, hold lock 3,2. for 
program 3, there is no data races happening, but the Eraser would detect it as data races. Is Eraser performing not well
 or do I have some misunderstanding?
- Tags: recitation
- Students' Answer: If there exist a shared variable x that 
occurs in all 3 programs then Eraser would detect a data race.  A datarace would not occur under the proposed conditions
 assuming shared variables are only used by programs 1,2,3 (if other programs use lockes we can get data races, 
espeically if shared variable occurs in other programs).   Of course this is a buggy implemenation and probally prone to
 deadlock but not dataraces.
- Instructors' Answer: 
# @591 Process
- Question: In recitation 4, what does process mean? Does it mean the PID when we are running a program? Or it means the
 current environment?
- Tags: recitation
- Students' Answer: 
- Instructors' Answer: 
# @589 Spring 2017 14 A
- Question: Why choose d for problem 13A? Shouldn't the window reduce by newW=oldW*(1-a/2)?
- Tags: exam1
- Students' 
Answer: Are you referring to p. 11, Q13?  http://web.mit.edu/6.033/www/assignments/old_quizzes/s18_1.pdf  It seems that 
the answer is (b), which should be compatible with your statement, unless I misunderstood your question.
- Instructors' 
Answer: 
# @588 Spring 2018 13
- Question: What exactly is Change 3? How is TCP related to delay-based scheduling? What are doing exactly for Change 3?

- Tags: exam1
- Students' Answer: Seems like this is addressing Spring 2017 for anyone reading this later.  My 
understanding of the question is that TCP as described in lecture is happening (i.e. sender ACKs, retransmit after 
timeout, which ACK you send depends on what you have so far, send things at the receiver exactly once in order, etc.).  
TCP isn't related to delay-based scheduling.
- Instructors' Answer: 
# @587 Spring 2017 5A
- Question: I am having some trouble understanding the lockset algorithm and the solution.&nbsp;  Algorithm:&nbsp;   
Procedure: 1. locks_held(t) = {lock_a, lock_b} 2. initiate C(x) = {lock_a, lock_b} and C(y) = {lock_a, lock_b} 3. line 
3's first access to x: C(x)=C(x)∩locksHeldC(x) = C(x) \cap locksHeld = {lock_A, lock_B} ????  I am super confused on 
when we removed lockB from C(x). Or am I understanding "access" incorrectly and the last time we accessed x was actually
 line 5, when we referred to x?&nbsp;
- Tags: exam1
- Students' Answer: I'm unsure if this answers your question, but I 
suspect that your statement "the last time we accessed x was actually line 5, when we referred to x" is correct.  
Specifically,  C(x) = a C(y) = a   Because x and y are respectively read and written when only lock A is held.
- 
Instructors' Answer: 
# @586 Lecture 3 Question
- Question: When we encounter a page fault, who calls "exception(x)"? Is it the MMU? Could a program running in user 
mode manually trigger an exception like this one?
- Tags: lecture
- Students' Answer: 
- Instructors' Answer: The OS 
will handle things like page faults so I think you could say they call exception(x) when triggered. Within exception is 
where we switch from user mode to kernel mode to handle the exception. In terms of manually triggering an exception from
 a program, this is possible (but likely from a different type of exception from a page fault, like an interrupt or 
trap)
# @585 2018 Exam 1.11
- Question: Why can a&gt;11a>11? The sender only sends packets up to 11, then how can a&gt;11a>11?
- Tags: exam1
- 
Students' Answer: The sequence given in this problem is of ACKs from the reciever, so as an example, what really 
happened could be something along the lines of:  This way, the right column excluding the ack the sender never got back 
still matches the sequence given in the problem, but 12 packets were sent in total. 
- Instructors' Answer: 
# @584 Sunday OH 3/27
- Question: Today's Sunday OH (normally 8-10) will be from 5-7 PM instead, same link as before! 
https://mit.zoom.us/j/93266461320 
- Tags: logistics
- Students' Answer: 
- Instructors' Answer: 
# @583 2018 Midterm Problem 7
- Question: In recitation, we mentioned that processes can only communicate through pipe but not shared memory. However,
 2018 Midterm Problem 7 implies that processes can also communicate through shared files. Is the file a pipe, or are 
there other ways to communicate between processes?
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: From the 
unix paper, “When a process is created by the fork primitive, it inherits not only the memory image of its parent but 
also all the files currently open in its parent”. While multiple processes can write to the same file, I don’t know if 
this can be considered a means of communication between two processes since they are just writing or reading to a file 
with no intended recipient. I think “shared memory” in the context of your question would be something like actual 
process memory rather than a file (which written to disk and considered “storage”).
# @582 Is there OH today?
- Question: ^
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: Yes it is the Sunday OH - will be from 5-7 PM 
today instead of 8- 10 PM
# @581 Exam 2019 Questions
- Question: 1.B: I am confused here why the answer is (b): a) You can learn this. Isn't this exactly what I learn from 
watching the traffic going in and out of the name server? The video explained this as "You are not going to learn (a) 
because as we said it is possible that the resolution for the name a.x is different in the cache of that name server 
than what it most currently is/should be". I think this statement is correct, but I don't understand what it contradicts
 the statement (a) b) You are not sure to learn nothing because of potential caching. It could have just as well be that
 this name server is the first name server that the user faces. Or you can see correct traffic now, so you are not 
learning nothing anymore. c) You can learn that. I am just not sure if that's helpful.&nbsp; You are also not sure to 
learn that here d) You can also learn nothing because the resolution starts at the root server. It is unlikely but it is
 possible to happen. I guess that mean it is not sure. The way I see it you can learn any of those, but none of them are
 surely gonna be learned. And choosing the BEST answer is a little confusing because I can't tell which is better to 
learn.  2.a)&nbsp;I thought this question was confusing because I immediately said yes because copy-on-write. Turns out 
the original UNIX paper doesn't implement this. I just wish on the exam that there is some space to explain our answers.
 Seems that with the above it is better to explain why I mean what I choose.  5.A)&nbsp;The explanation is that if X 
sends something, while Y is sending it gets something from X, it will detect a collision and flood the network. The 
travel time for X sending and then flooding is RTT, but I don't understand why is RTT is useful for determining a 
collision. We determine a collision because the transceiver detects a carrier on the wire. This case also doesn't have X
 and Y sending simultaneously (X sends and then Y sends as it is receiving from X).  5.B.d) The video explanation was 
also a little confusing. It was something along the lines that the transceiver fails and starts writing random things to
 the ethernet, nothing will be transmittable. This is correct, but this happening seems a little arbitrary. We didn't 
really define what failure means in the class or the type of failures in literature. In my head, a failure of something 
just means that it stops working, and that's how I understand it is being used in the literature. And if according to 
the question we can assume that under a failure anything could happen, then anything can happen as a result? If we 
assume that a failure could cause a processor to do some deterministic arbitrary thing, then most of our systems 
wouldn't be correct ig.&nbsp;  6.C.c)&nbsp;The answer was False because not necessarily. That's also really confusing. 
Why is the question asking about a completely arbitrary detail and then the answer is no because it is arbitrary? Most 
of these protocols would probably be implemented in C or a similar language. I would actually assume if somebody where 
to implement a path minimization problem with integer values that they would set infinity to TYPE_MAX, it makes the code
 simpler and faster, than having to write some check or tag the integer with a boolean saying it is infinity.&nbsp;  
8.B) The question is asking "XA still wants to send traffic to XC". Why do we need to consider XC sending back to XA 
(i.e. both ways)? In any case, why wouldn't (c) be sufficient for both ways? The way I understand RON is that there is 
some software running on some server somewhere that is connect to some provider. If somebody in XC is running a RON 
application, they can send traffic to the RON server in B because in general, they can send traffic to B. The RON server
 will take the traffic and reroute it to the RON server in XA. Eventually, the RON server in XA will send the traffic to
 the receiving end in XA  I am also curious about the statics for this exam: mean, ...&nbsp;  In other systems classes I
 have taken before, we got just questions and we had to write a couple of sentences as an answer. I thought those exams 
were much easier than here; I found the choices a little confusing and I thought there was a gap between what the 
question had in mind and how are the choices were phrased. I just hope at least there are big spaces on the exam paper 
so I can explain everything. I know the exam instructions says to explain you assumptions, but it is very easy not to do
 that during an exam if you think the the assumption you are making is a fact rather than an assumption (at least in 
your head) and you only need to do multiple choices.
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: 
# @580 Meaning of parameters for RED/ECN, DRR, and WRR
- Question: I saw this in question 14 of Spring 2018, and I was wondering what are the quantum parameters for DRR and 
WRR? Is there also an explanation for the parameters that can be tuned for RED and ECN, like in question 13 of spring 
2017?
- Tags: exam1
- Students' Answer: Quantum is like "credit" -- if you don't send a lot in a round or you don't have
 enough credit to send (maybe you have like 20 quantum but like a packet of 100 size) then you just accumulate quantum.
  Think of it as flexibly rationing a fair portion of the bandwidth, and giving the queue the option to spend it 
whenever, according to the size of the packet it has.  There's a good illustration of this at the end of lecture.  For 
RED and ECN, the parameters are:  p_max = the max probability with which you are going to drop/mark packets q_min = the 
min queue size before which you are not going to drop any packets q_max = the max queue size you will tolerate -- after 
this you drop with probability 1, because you aren't going to accept any more  There's a piecewise graph of this in 
lecture to better explain what it means.
- Instructors' Answer: 
# @579 Spring 2018 exam 1, problem 3
- Question: For filling out the shadow page table in this question, why is W set to 0 for guest virtual = 3? Would there
 be a page fault if W = 0 and you are writing to the page?&nbsp;
- Tags: exam1
- Students' Answer: @604 @575
- 
Instructors' Answer: 
# @578 Mapreduce
- Question: Are we suppose to know the map reduce algorithm that came up in midterm 2017? If so, where should we find 
the content?
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: 
# @577 Virtual Memory
- Question: Is it possible for the virtual address space to be larger (or smaller) than the physical address space?  
Thanks!
- Tags: lecture
- Students' Answer: Yes, virtual address is larger typically. In lecture recall the 
virtualization is to let every process think they have the entire space to themselves -- I think this is why it's 
possible to call pages from disk. Instructor please confirm if the latter is right.
- Instructors' Answer: 
# @576 Page Table Entries (L3)
- Question: Is the additional information in a page table entry always 12 bits long? For example, if the page number was
 12 bits long (instead of 20 bits), would the page table entry be 24 bits long (instead of 32)?  Thanks!
- Tags: lecture

- Students' Answer: If you mean virtual page number vs offset, then those are determined such that the sum of their 
lengths is the length of your entire address. What length your overall address is, and what virtual page number you have
 (or, what length your overall address is, and the length of your offset) determine the third thing. But they don't have
 to be 32 or 20 or 12 or anything like that specifically, as far as I know.
- Instructors' Answer: 
# @575 Questions about 2018 Q3/Virtual Memory/Emulation
- Question: p. 3  http://web.mit.edu/6.033/www/assignments/old_quizzes/s18_1.pdf&nbsp;  1. The question says "the 
content of that [shadow] table may differ depending on whether the guest OS has its U/K bit set to U (user) or K 
(kernel)." How would it differ if the guest OS was in user mode? When would the guest OS go into kernel vs user mode?  
2. Why can the W and U bits not be discerned in row 1?  3. When it says that the VMM is tracing writes by setting W to 
0, what does it mean? What precisely is being set to read-only, is it the page table that belongs to the guest OS?  4. 
Why is row 4 requiring W = 0 but not row 1 or 5?  5. The problem states that when the guest OS sets itself to K the 
shadow table should correspond to that. Why are the two bits in the box marked as 1? And what is meant by "Guest OS in 
user mode" and what do those bits control?
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: 
# @574 Quiz 2017 Routing B
- Question: I don't really understand why x still knows about y and vice versa if peering is removed between A and B. I 
thought y would in this case only know about B, C, z and T2. How does it know about a route to x?
- Tags: exam1
- 
Students' Answer: If A and B aren't peers but T1 and T2 are, then A tells x about T1 (it can charge more for transit 
along x-A than A-T1). Then, T1 will tell A about its path to T2 (tell customers everything you know), T2 will tell T1 
about B because tell everyone about your customers, B tells T1 about y because tell everyone about your customers.  For 
y to x you can do the same argument but in reverse order.
- Instructors' Answer: 
# @573 Quiz 2017 Routing
- Question: http://web.mit.edu/6.033/www/assignments/old_quizzes/s17_1.pdfI remember that in class we said that "AS 
exports *only* customer routes to peers" but then I don't really understand why it's not beneficial for A to inform x 
about their potential access to Z. I know that the rule is that provider only informs about its customers (and itself) 
but from the policy point of view, I don't really understand why the following is not true. Since communication between 
A and B and C is free and x gives money to A to get access to y (and x can send to y), why it's not equivalent to A 
letting x know about z. The only difference would be introducing traffic between node B and C, which is for free.
- 
Tags: exam1
- Students' Answer: 
- Instructors' Answer: 
# @572 old quizzes?
- Question: Question @566 mentions that there are older quizzes available. How do we find these older quizzes?
- Tags: 
exam1
- Students' Answer: Under Calendar >> Exam 1, or https://web.mit.edu/6.033/www/assignments/exam-1.shtml this link

- Instructors' Answer: 
# @571 Lecture 8 TCP question
- Question: In lecture 8's outline, I have a question about the comment on TCP:   Why add it [a congestion control 
mechanism] to TCP, not as a separate layer? It was already hard to add a new layer, even in the 80s.    Just to clarify,
 adding the congestion control mechanism to a pre-existing layer forces all current devices to accommodate for that 
update. Whereas by adding a new layer, some devices may circumvent/opt-out of that functionality. (This is my 
understanding, correct me if I'm wrong)  How is it 'harder' to add a new layer rather than just updating an existing one
 then?
- Tags: lecture
- Students' Answer: 
- Instructors' Answer: Congestion control isn't added to a "layer"; it's 
part of TCP (i.e., it's part of a protocol, not an entire layer). If you use TCP, you get both reliable transport and 
congestion control. If you want congestion control but not reliability, then you're out of luck.  Another option 
would've been to, say, build a congestion control layer that lived "underneath" the transport layer. Then any transport-
layer protocol (TCP, UDP) would have the option of using (or not) congestion control. But if we want to add this new 
layer, now all devices need to accommodate it (it would add a new layer of encapsulation, for instance). Even in the 
80's, it was hard to make such a big change.
# @569 lec2 gb from table size question
- Question: In Lecture 2's 'all-animation' slide 30, it states: '2^32 virtual addresses each mapping&nbsp;to a 32-bit 
physical address -&gt; 16GB to store this table'  How does it take 16GB? I'm not very good with the GB &amp; MB 
notation, but google says 1 gigabyte = 2^30 bytes. So I figured the table would take 2^32 bits as 'searchable keys' 
alongside its mapped 2^32 bit value.&nbsp; I understand that would be (2^32)*2 = 2^33 bits required for size. But the 
slide saying 16GB is 16*(2^30)*(2^8) = 2^42 bits.&nbsp;
- Tags: lecture
- Students' Answer: 
- Instructors' Answer: I 
think the 16GB number just comes from 2^32*32 bits converted to GB. The table would in theory only hold the 32-bit 
address, and would be 2^32 entries long, indexed by address.
# @568 What happens across all layers when I make an HTTP request?
- Question: I'm reviewing some of the lectures and recitations and trying to piece together what happens under the hood 
when I make an HTTP request. When I make a get request to google.com this is my understanding:1. HTTP request is written
 as a data payload at the application level2. Some header is added in TCP in the transport layer that contain port 
numbers? (What specifically is added to the header)3. We use DNS to find the IP address of google.com, add this and 
relevant info into the IP header4. Then the IP packet is sent through the ethernet and across network boundaries5. This 
then enters the physical layer and eventually finds its way at some server containing the data I want6. The above steps 
then happen in reverse.Is my understanding correct? What data is added in the TCP and IP header and how is it obtained? 
Why did we bother to separate TCP and IP anyways? Edit: Where does exchange of cryptographic keys come in?
- Tags: other

- Students' Answer: 
- Instructors' Answer: 
# @567 Access to files on the 6.033 website
- Question: Can we assume we have access to all files on the 6.033 websites? So lecture slides, recitation readings, 
etc. Or do we have to actually download all of them to access them locally? Thanks
- Tags: exam1
- Students' Answer: 
- 
Instructors' Answer: Download them. We really just want you to turn off all network connections while you're taking the 
exam.  Additionally, we can't guarantee good Internet access during the exam (34-101 typically has decent access, but I 
don't know that Walker is set up for many people using a network at once). It'd be a risk (admittedly minimal, but 
nonzero) to rely on material that was only accessible via the Internet.
# @566 Explain Spring 2015 14A,B
- Question: I was told by a TA that the older quizzes were still helpful and permissible to use.  On p. 11 
http://web.mit.edu/6.033/2016/wwwdocs/assignments/old_quizzes/s15_1.pdf  Could you please explain how to arrive at the 
answer for 14 A and B?
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: 
# @565 TCP fast retransmit/fast recovery
- Question: In the slides, the graph for window size against time(RTTs) we can identify when AIMD is happening or slow-
start is happening but is there a way to identify from the graph that fast retransmission/fast recovery is happening?
- 
Tags: exam1
- Students' Answer: 
- Instructors' Answer: Yes. TCP has two mechanisms for handling a lost packet: * Fast 
retransmit/fast recovery: When a TCP sender sees four total ACKs with the same sequence number, it will immediately 
retransmit the next packet in the sequence number space, because it assumes it has been lost. In response to this lost, 
TCP cuts its window size in half. * Retransmission due to a timeout: If a packet times out and forces the 
retransmission, TCP will retransmit the packet, and drop its window all the way back down to zero (slide 16 here).  So 
if you're seeing the normal TCP "sawtooth", you're seeing losses handled with fast retransmit/fast recovery. If you see 
a drop to a window size of 1, you're seeing timeouts.  In practice, fast retransmit/fast recovery handles the majority 
of loss. If a retransmission is caused by a timeout, that typically means there has been significant loss (typically 
multiple packets in a row).
# @564 Spring 2017 16B
- Question: Could you please explain the answer?  http://web.mit.edu/6.033/www/assignments/old_quizzes/s17_1.pdf p. 15
-
 Tags: exam1
- Students' Answer: 
- Instructors' Answer: We didn’t learn TDMA this term, so I wouldn’t worry too much 
about this question
# @563 Spring 2017 10B
- Question: http://web.mit.edu/6.033/www/assignments/old_quizzes/s17_1.pdf p. 11  Why B can't be c or d?
- Tags: exam1
-
 Students' Answer: I think it is because, according to the problem description, S has not retransmitted any packets. 
- 
Instructors' Answer: 
# @562 Spring 2017 8B & general question about BGP
- Question: http://web.mit.edu/6.033/www/assignments/old_quizzes/s17_1.pdf  p. 9  I tried to figure out all of the nodes
 that every client has access to.  When A and B peer but T1 and T2 don't:  x: A, T1, B, y y: B, T2, A, x, C, z z: C, B, 
y, A, x  When A and B don't peer but T1 and T2 do:  x: A, T1, T2, B, y y: B, T2, T1, A, x z: C, B, y  This implies that 
A and B do provide connectivity from z to A and x, which is wrong.  Could you please: 1) confirm if my reasoning above 
is correct for who can reach who, and if not, what you got for the reachable destinations, 2) explain where I went wrong
 in my reasoning about A and B providing extra connectivity? 
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: 
I think the statement that “z: C, B, y, A, x” can happen when A and B peer is where this is incorrect. In both cases, it
 would just be “z: C, B, y”. From my understanding, B and C having a peering agreement provides no incentive for A and B
 to make their peering relationship known and available to C, so z will not reach x or A. See also: @610
# @561 Spring 2017 5b
- Question: Possible that I am overthinking this, but I understood the problem to be the following:  (c) requires that 
all sources of concurrency are eliminated, not just some. Since get_balance releases balance-lock, it's possible that 
get_balance is interrupted before the return, transfer modifies balances[account], then get_balance returns an outdated 
balance to whatever function called it. Therefore, the answer is (d).  Could you please point out where I went wrong?
- 
Tags: exam1
- Students' Answer: 
- Instructors' Answer: We may go into this more in upcoming lectures (about 
transactions and consistency guarantees for example), but the locks have the effect that we are now ordering the 
get_balance and transfer operations in some way and each operation in atomic. I think the question in © is that you 
eliminate [some] sources of incorrectness, not necessarily all. And this change does so by ensuring that no client will 
see a balance mid-transfer, only before or after a transfer. edit: I said atomic but I really meant no interleaving 
between parts of each operation
# @560 Are virtual page sizes and physical page sizes always the same size?
- Question: i.e. is the number of bits describing a VPN the same as a PPN, always?
- Tags: exam1
- Students' Answer: 
- 
Instructors' Answer: For the most part, the answer is yes (4KB).  As a quick aside, modern CPUs often support large 
pages (e.g., 2MB), and in this more complex situation, the VPN could be larger (or smaller) than the PPN.
# @559 Virtual Machine Monitor
- Question: Our discussion from lecture says that there are two ways we can run multiple OSes on a single machine:  
A.&nbsp; Run it as a user-mode application inside the host OS or  B. Run it as a kernel-mode application with the guest 
OSes in user mode.&nbsp;  If we do A, how is the VMM going to be able&nbsp; to handle things like virtualising hardware 
for the guest OSes when it is not running in kernel mode? I'm struggling to see how such a setup will actually work.  If
 we do B, does it just mean that we are simply designating the VMM as the OS and the host OS just becomes another guest 
OS like the&nbsp; other ones? I am also struggling to understand where the host OS fits into all of this.  Thanks!
- 
Tags: exam1
- Students' Answer: 
- Instructors' Answer: 
# @558 Sunday OH 12-2 cancelled this week 3/27
- Question: As the title says, they will pick back up the following week. Hope everyone is having a nice break so far.
-
 Tags: logistics
- Students' Answer: 
- Instructors' Answer: 
# @557 Are there OH during the break (this week)?
- Question: ^
- Tags: logistics
- Students' Answer: 
- Instructors' Answer: No office hours during the break, but 
they'll pick back up next week!
# @555 2017 Exam 1, problem 2c
- Question: Would the statement in 2c be false no matter what commands are used? So if the second command was not grep, 
would there still be blocking on the first process?
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: The two 
processes with a pipe between are already running in parallel (no matter the command). The latter command may be 
blocking for the input coming through the pipe from the first commands output, but this is not the case for every 
command. Some commands, like ls don’t really take an input (try something like yes | ls in your terminal!).
# @554 2017 Exam 1, q1
- Question: I was a little confused on how to do parts b and c of this question. For part b, is there an explanation or 
walk-through behind how to reason with the inner and outer page tables? Similarly, is there reasoning for part c?&nbsp;

- Tags: exam1
- Students' Answer: (b)  k entries for each line in every page table.  Maximum number for Mark: You need 
2^m for the outer page table because there are m bits, so they specify 2^m indices of k length each. Each of those maps 
to a separate lower-level page table with indices specified by n bits, so that's why 2^n for each of those tables.  
Maximum number for Pete: 2^(m+n) because you have m+n bits per index.  Minimum number for Mark: You need one outer table
 of size 2^m. Hierarchical page tables only allocate lower-level page tables when needed, so you need one for the one 
memory access, hence one lower-level page table of size 2^n. See the maximum number for Mark for why 2^m, 2^n.  Minimum 
number for Pete: Same reasoning as maximum number for Pete, you need allocate the entire table no matter what if there's
 a single memory access (discussed in lecture).  (c)  For choices (a), (b):  Think of it this way: Let q be the number 
of bits dedicated to the virtual page number. Then, p + q  is a constant (because you increase and decrease the two 
components by the same amount).  Then, you have 2^p page tables of 2^q addresses. So, 2^(p+q) addresses total. Since p+q
 is constant, so messing with the distribution of p and q doesn't affect the number of entries.  For choices (c): This 
doesn't help because looking at the maximum number of bytes allocated for page tables: The bytes that correspond to 
actual addresses is the k (2^(m+n)) bytes (the lower-level page tables). So, it's still the same 2^p number of page 
tables, so the same number of entries overall.
- Instructors' Answer: 
# @553 Participation Check in #2
- Question: When should we expect check in grades to be posted on canvas?&nbsp;
- Tags: logistics
- Students' Answer: 
They've started posting them - I got my grade on Canvas yesterday.
- Instructors' Answer: Please reach out to your TA if
 you haven't received these yet!
# @552 Modules vs. Components
- Question: Hello, I took a look at the DPPR and saw this section:  "[DPPR] Introduces a system, from overview to 
modules to components and communications"  I was wondering what the difference between modules and components were.
- 
Tags: design_project
- Students' Answer: 
- Instructors' Answer: 
# @551 Listing Too Many Design Priorities in Intro of DPPR
- Question:  In the rubric for the DPPR, one undesirable quality of the introduction is listing 3 or more design 
priorities in the goals section of the introduction of the DPPR. However, I'm not really sure what this means. The 
system has many goals (power sharing, dealing with outages, collecting info for billing/research, etc.) and it seems 
like if we do not list all of these, we are just not being thorough and not fully describing the system. Can you clarify
 what exactly you're looking for in the introduction?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer:
 Think about which ones you consider most important. We are asking you to prioritize up to three of them and explain you
 choices.
# @550 Using prep assignment in DPPR
- Question: Can we re-use sections of the prep assignment in the DPPR (in intro, conclusion, etc.)&nbsp;
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: Yes.
# @549 2017 Exam1 Number 7
- Question: Would someone be able to explain both parts of number 7?&nbsp;  For part a, I don't understand a few things:
 - Is the role of the default name server to store the locations of the root servers? - I don't understand the 
explanation for why C2 is also 4R. If C1 and C2 both access the same default name server, wouldn't N have cached 
www.a.com no matter what client is requesting it?  For part b, why does the time for C2 exactly? I don't understand the 
explanation given.
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: In the question set up we are told some 
important things:   In part a: In part b: 
# @548 2019 Midterm Video Explanations
- Question: The TAs from both last year and this year have filmed video explanations for each of the problems on the 
2019 midterm. All the videos can be accessed here:  
https://drive.google.com/drive/folders/1K6efVRwUgZnW7opYPsYnNzcghXfuOfbn?usp=sharing &nbsp;  Hope you all find these 
helpful, have a good spring break and good luck on the exam!
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: 
# @546 Lecture notes?
- Question: If these already exist, could these please be posted? They are very helpful in reviewing material. (For 
example, if the instructor already has an outline/script for the lectures?)
- Tags: exam1
- Students' Answer: 
- 
Instructors' Answer: I post notes for every lecture on the calendar; they're linked to from each individual lecture. (I 
typically post them the day after lecture)
# @545 Word Count
- Question: Our current DPPR is 3400, is being over by this amount okay?
- Tags: design_project
- Students' Answer: 
- 
Instructors' Answer: @438  3400 is pretty far over -- you might be giving too much detail
# @544 Exam 1 Logistics
- Question: Exam 1 is coming up! We've already posted practice exams to help you review, and their are lecture slides, 
lecture outlines, and recitation notes all linked to from the calendar.  The exam is scheduled for 7:30pm-9:30pm on 
3/31. It will take place in 50-340 (Walker) and 34-101. Last names A-O go to Walker; P-Z to 34-101. (Further details 
here.)If you cannot make the scheduled exam time because of a class conflict, please fill out this Google form to help 
us schedule a make-up exam for you. If you need a make-up because of a class conflict, we need to know by the end of the
 day on Monday, 3/28 (but the earlier the better).If you have accommodations from Disability and Access Services, you 
should've gotten an email from me earlier today. Please reach out (lacurts@mit.edu) if not. 
- Tags: logistics, exam1
- 
Students' Answer: 
- Instructors' Answer: 
# @543 Is there tutorial today?
- Question: It's not on the calendar?
- Tags: tutorial
- Students' Answer: 
- Instructors' Answer: There is no tutorial 
today!
# @542 DPPR Extension (Group or Individual)
- Question: Resolved. I understand now extensions are granted to groups.
- Tags: design_project
- Students' Answer: 
- 
Instructors' Answer: (Just answering here so this shows up as resolved)
# @539 Stop using power from solar panels
- Question: Is it possible to not use energy from batteries connected to solar panels but switch to central utility even
 when batteries are connected to the solar panels have non-zero energy left? More precisely, let’s consider the 
municipal building microgrid. Is it possible for us to direct buildings to use electricity from central utility instead 
of the solar farm if the capacity of the solar farm decreases below say 30%? The 30% minimum might come in handy when 
there is an unexpected power outage and the microgrid is cut from the central utility.
- Tags: design_project
- 
Students' Answer: 
- Instructors' Answer: At present there is no way to do this.
# @538 Sharing with central utility
- Question: From my current understanding, share_on or share_off only affects sharing in the local loop. Is there a way 
not to share power with central utility even above threshold? For example, the threshold is set at 50% and power sharing
 is off. Is it possible to avoid sharing with central utility even if the power storage is above 50%?
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: At present there is not.
# @534 Smart meter records
- Question: When a house uses energy from its solar panel battery, on which smart meter is this power consumption 
recorded- the one for incoming or outgoing energy. I'm confused because in one of the piazza posts i saw that "smart 
meters on the solar panel systems only count power when that power is on the line going back to the CMLC", which would 
imply that either we don't record that use at all or we record it on incoming energy smart meter. For the smart meter 
that measures incoming energy, does it count power from both CMLC and local loop and it cannot differentiate between 
these 2 sources automatically?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: Every smart meter 
counts power on the lines connected to the central utility, but they cannot observe direction. So, the smart meters 
attached to the solar panel systems count the power that is being transmitted from the batteries to the central utility.
 The other smart meters count the power from the central utility used by that customer.  That said, each smart meter is 
capable of measuring three types of things, power generated, power stored in the batteries and power passing through the
 lines with the central utility. Notice that for the smart meters attached to solar panel systems, the first two of 
these are meaningful because there is a capability to generate power and store it. But for the other type of meter, 
those values will always be zero, so those smart meters will have readings of the power that exchanged.  Also, note that
 for the smart meters measuring incoming power, this does not include power coming  on the local loop, from other houses
 in the microgram. Those are just not counted. Because there are two wires coming into each house, one from the utility 
and one from the local loop, it is simple to just have the local loop bypass the smart meter. You don't need to design 
this. It is given to you this way.
# @533 What is a local loop?
- Question: If a house's 2 smart meters connect to/from the solar pannels from/to the power plant, is a local loops just
 wiring? Are there smart meters along a local loop? Do the smart meters pass by the microgrid as they go to the power 
plant?
- Tags: logistics, design_project
- Students' Answer: 
- Instructors' Answer: The local loop is an electrical 
loop that connects the houses in a single microgrid. It is the facility by which the solar panel systems within the 
microgram can share any excess power above the individual thresholds with others in the microgram. The whole thing is 
set up so that a house will only take power from the local loop if its batteries are empty. There is no direct 
accounting for this sharing.  I'm not sure what you mean by the smart meters being "along a local loop". They are 
attached to residences, buildings and solar panel systems, but they exchange data not electricity whereas the local loop
 carries electricity.  The smart meters are not in direct contact with the central utility.
# @532 How does an individual house get credit for sharing from a microgrid to central utility?
- Question: How does an individual house get credit for sharing from a microgrid to central utility?
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: I'm not sure which part of this you don't understand. There 
are two things going on, electricity and records of electricity transmitted. Electricity is transmitted through the 
electrical system of the house onto the wires that connects to the central utility. If the house isn't in "sharing" on 
the local loop mode, any excess power in the local batteries that is above its threshold is offered to the central 
utility. If the central utility batteries are not full, it will take that offer.  If that happens, then that information
 is measured by the smart meter attached to it. It keeps records, taken every 15 seconds. They measure (among other 
things) how much power the solar panel system has contributed to the central utility. Those records need to be 
transferred to the microgram controller and then to the central utility. So, the initial record keeping is in the meters
 themselves, but the central utility needs to know all this. On a monthly basis the central utility counts up all the 
records of the power contributed by each house and includes a credit for that amount on the monthly bill.
# @531 Apartment Building Smart Meters
- Question: What do the smart metes record? Our thought was this 1) The smart meter on the roof tracks the outgoing 
power, which can go to either the other buildings or the central utility. 2) The smart meters in each apartment track 
power generated by the solar panel, the power stored in the battery, and power going in. Is this correct?
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: The meter for the panels tracks the energy that they generate
 and the meters for the apartments track the energy that they consume.
# @529 Are there no OH eom
- Question: 
- Tags: logistics
- Students' Answer: 
- Instructors' Answer: Sorry for a late response, but there were 
virtual OH 4-6pm today.  In the future, you can join at the queue here:  https://queue.mit.edu/6.033/queue Let us know 
if you had any trouble joining!  The full schedule is listed here:  http://web.mit.edu/6.033/www/hours.shtml 
# @528 DPPR: routing protocol needed?
- Question: Hello,  Looking at one of the example DPPRs (ABETS), they mention "onion routing" in their system design. Do
 we need to get that specific on our DPPR (mentioning a routing protocol) or can we just describe generally what 
information flows through our network?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: Every DP is 
different and focuses on different things. In this case, routing isn't an issue.
# @526 Drawing system diagram
- Question: Is there any good tool for drawing system diagrams neatly?
- Tags: design_project
- Students' Answer: 
- 
Instructors' Answer: There was an answer to this a while back, which I can't find right now. Personally, I use 
powerpoint and then create pdfs of my drawings to insert into my text. I know that's crufty and old-fashioned, but for 
me it's easier than learning something new. But go back through the piazza questions for another recommendation.  
(Update from Katrina: check out @337)
# @525 DP Power Sharing Questions
- Question: I have a couple of quick questions about when power is shared between the central utility and the microgrid.
 I know that these questions have been asked before, but I'm still a little unclear, so I just wanted to quickly clarify
 them.&nbsp;  1. Assuming that none of the houses in a microgrid are below their minimum, when will a house start 
sharing power with the central utility? Will it share once it is above its minimum, or will it wait until it is at 100% 
and can no longer store any additional energy?  2. When will the central utility stop providing energy to a house? Will 
it stop once the house is above 0% or will it wait until the house has reached its minimum threshold?  Thanks!
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: 1. The house will share with the central utility whenever its
 own batteries are above the house's threshold. This will definitely be below 100%.  2. As long as the central utility 
has access to power (from its own batteries or the regional utility) it will always make power available to every 
customer. They do not need to use it, but the contract is to provide the 100 or 200 amps to every residence.
# @524 Canvas Assignment - Recitation 13
- Question: Hello! I don't see an assignment on Canvas for the Rec 13 reading questions. Can one be made? Or should I 
just email my TA my answers?
- Tags: recitation
- Students' Answer: 
- Instructors' Answer: should be posted now - 
sorry!
# @523 LTE limit
- Question: The spec says that we have a 2GB LTE limit on each controller and smart meter. How is the communication 
between central utility and controller included in the limit? For example, if central utility sends 1MB message to 
controller, then do we count it as using up 2GB limit? If controller sends 1MB a message to smart meter, is this 
subtracted from controller limit or smart meter limit or both? Thank you!
- Tags: design_project
- Students' Answer: 
- 
Instructors' Answer: Yes, the student response is correct. Please go back and read previous questions and answers. I am 
in a rush right now, but this has been answered previously.
# @522 Receiving power from another house in microgrid
- Question: If a house is receiving power from another house in the microgrid, does it keep continuously receiving power
 as needed (for current usage), or will it use that to charge its own battery to make it above the threshold? (in other 
word, is it a pay-as-you-go model or we receive a big amount to charge our battery and then stop the communication)?
- 
Tags: design_project
- Students' Answer: 
- Instructors' Answer: This actually is in a number of previous questions, but
 for the quick answer, there are several parts. If a house needs power and others in the microgrid are above their 
thresholds and they have been requested by the microgrid controller to share their electricity, the original one can 
keep receiving. But, that said, the receiving one will never recharge its batteries from the power lines. That 
recharging happens only from the solar panels. The only battery system for which this is not true is the system run in 
the central utility itself, which has no solar panels.
# @521 Question about Storm Scenario
- Question: As I understand it, there are two parts to the storm scenario: 1) The central utilities' ability to 
communicate with anything else gets cut off. 2) The literal power lines that distribute energy from the central utility 
to meters get broken for half of the microgrids.  But it also seems to me that Issue 2 is entirely subsumed by Issue 1, 
in a sense? If the central utility cannot communicate with the microgrid controllers, how is anyone going to receive 
power from the central utility? The central utility would have no ability to turn the power flow on for a given 
meter.&nbsp;  The other possibility I considered is that the "state" of power flow between the central utility and any 
given meter gets frozen when the central utility's ability to communicate gets broken: Any meter that is currently 
getting power from the central utility will continue to receive it even if they don't need it, and the microgrid 
controller is unable to make requests for meters that do need power that currently aren't getting any.  Which of these 
two is the correct scenario? Or have I made a wrong assumption somewhere else?
- Tags: design_project
- Students' 
Answer: 
- Instructors' Answer: You are right about the two stages of the scenarios, but not quite right about what is 
going on. The electrical system will deliver power to the homes independent of whether the central utility can send to 
or receive from the microgrid controllers and the same for the smart meters. The electricity runs on electric wires and 
the bits flow on the broadband or LTE connections. Remember we had a reasonably well working electrical system long 
before there were smart meters and microgrids. The basic electrical system was there first. But, if it's wires are down,
 it can't deliver electricity.
# @520 Do smart meters automatically stop counting power usage when share power is on?
- Question: When share power is on, we only want to be distributing power within the microgrid to even out battery 
levels.The smart meter on the house that is getting its battery filled will see power coming in to the household, and 
the smart meters that are sharing power will see power leaving their household. However, this transaction should be 
free. Will we need to discount this power usage from the meter readings, or will the meters not record any usage 
automatically?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: The smart meters on the solar panel 
systems only count power when that power is on the line going back to the CMLC. Otherwise, the power does not go through
 the meter and it can't count it.
# @519 Security Concerns
- Question: Is there any privacy concerns with the lossless aggregated data such IP addresses of the smart meters? 
&nbsp;While it may be in safe hands with the researchers it may permit malicious attacks.
- Tags: design_project
- 
Students' Answer: 
- Instructors' Answer: Good question. In the list of questions at the end, the last one is about 
privacy. We haven't talked about that yet, so we don't expect you to address it, but it can definitely be an issue in 
systems like this. If you'd like to comment on it, your readers might find that interesting.
# @518 Gradescope has no grade but got it in Canvas
- Question: My networking hands-on has a grade in Canvas but not in Gradescope. Is this expected?
- Tags: recitation
- 
Students' Answer: 
- Instructors' Answer: It's not! Try now.
# @514 Can central utility cut off power lines?
- Question: Is the central utility able to prevent power from being sent to certain microgrids from its own power 
source? (This could be useful in the case of a power outage to make sure power only gets sent to essential areas.)
- 
Tags: design_project
- Students' Answer: 
- Instructors' Answer: Yes. See @512
# @513 Rate of battery draining
- Question: When a battery is returning power to the central utility, how quickly does this power transfer occur (that 
is, how fast does the battery drain)?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: 
# @512 Sending power over broken lines?
- Question: What happens when the central utility attempts to send power to the microgrid controllers when one of the 
power lines between the central utility and the microgrid is broken? Will the central utility be able to detect when the
 power line is broken? Will there be any safety concerns?
- Tags: design_project
- Students' Answer: 
- Instructors' 
Answer: Yes they will be able to detect it. What happens is that the wires are live. So, the utility will need to turn 
off the power to that line very quickly so they don't electrocute anyone or start a fire. The utilities know how to do 
this. We get trees down in New England fairly frequently. They get wildfires from these in the West. So, they work very 
hard to turn off that power very quickly.
# @511 Purpose of Solar Panel farm minimum?
- Question: If the solar panel farm contains the only batteries that are in the microgrid for the public utilities 
(hospital, police station, fire department), what is the purpose of having its battery threshold automatically set to 
75%?  From my understanding, it's impossible for it to share power with other microgrids and it will only share excess 
power with central utility, so I can't find any significance to this number.  Thank you!
- Tags: design_project
- 
Students' Answer: 
- Instructors' Answer: 
# @510 Extensions on DPPR (and anything else)
- Question: I got a few questions today after class about the DPPR, so I wanted to remind everyone of the late policy in
 6.033. It's here, but most importantly:  "If you're unable to hand in an assignment on time, reach out to your TA. As 
long as you let your TA know before the deadline, you can assume that we will give you at least a 24-hour extension on 
the assignment. If you feel that a longer extension is necessary, we'll work with you (and perhaps S3) to come up with a
 plan."  In addition to extensions, we're also ready and able to help with any DP team issues. But you have to tell us 
about them! We can't help with things we don't know about.
- Tags: logistics, design_project
- Students' Answer: 
- 
Instructors' Answer: 
# @508 Can we assume Battery Efficiency?
- Question: Can we assume complete battery efficiency for our designs?  For example, if we buy $$x$$ kWh of electricity 
from the power plant and store it in the central batteries, can we assume that we can then redistribute the full $$x$$ 
kWh to the various microgrids? Or if those $$x$$ kWh are stored into the central batteries on one day, but then never 
used for a week (or more), can we assume that the battery doesn't slowly lose charge over the following days?Or do we 
need to take into account the (real-world) inefficiency of batteries to try to design a system that uses as little 
energy transformation as possible?  Also (I think it would be outside of the scope of the class to account for this), I 
am assuming we do not need to take into account the degradation of batteries over repeated charge/discharge cycles 
and/or time.
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: Yes and yes. for our purposes here 
assume perfect batteries. No loss and no degradation. 
# @506 Extended Data Plan Question
- Question: Are we able to purchase the extended data plan for individual microgrids, or is the plan only purchasable 
for all components of the system?&nbsp;&nbsp;
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: I'm 
confused. There is no mention of an extended data plan as an option. Where are you seeing that?
# @505 solutions to hands on?
- Question: are the solutions to the hands-ons posted anywhere? i keep getting points off and sometimes there are no 
helpful comments associated with the point deductions, so i would like to know what the right answers are instead of 
continuing to (erroneously) think my current understanding of concepts is correct
- Tags: handson1, handson2, handson3, 
handson4, handson5, handson6
- Students' Answer: 
- Instructors' Answer: 
# @504 Intervention statement
- Question: The answer to @348 mentions an intervention statement. What does this mean?
- Tags: design_project
- 
Students' Answer: 
- Instructors' Answer: Yes, as the student below states, it's really just another way of saying 
solution statement. It's stating what approach you're bring to the table to solve the problem.
# @503 Clarify role of Internet & LTE in communication between microgrid controller & central server
- Question: My understanding is that the LTE is used to communicate between the microgrid controllers &amp; central 
server (as well as communicate between the microgrid controller &amp; its smart meters), and the internet is only 
necessary for the central server interfacing with the outside world.  In this case, when the storm use case presents us 
with the fact that the internet goes down, that just means the central server can't do things like purchase external 
power for the town, or relay data to the researchers, for that 12-hour period.
- Tags: design_project
- Students' 
Answer: 
- Instructors' Answer: Not quite. All the devices that are using LTE only are "on the Internet". Those are the 
smart meters and microgrid controllers. This is the same has you using a data plan on your phone. That is using LTE but 
let's you get to Facebook, web pages, etc. The central utility is "on the Internet" via the broadband connection. That's
 what Facebook and web servers are typically doing. Those are their "link layer" protocols/technologies on top of which 
they support IP, etc. Every device has an IP address, just like the world we live in.  But, they are constrained as to 
which other devices they can communicate with. Each smart meter can only communicate with its microgrid controller (not 
the other smart meters). Each microgrid controller can only communicate with its smart meters and the central utility. 
The central utility can communicate with the microgrid controllers and the rest of the world (if you think you need this
 for some reason).  Separately, if the network goes down (e.g. the central utility can't communicate with the microgrid 
controllers or the microgrid controllers and smart meters can't communicate) the central utility can still use 
electricity from the regional utility. There are two very distinct networks here. One is the data network that involves 
the central utility, microgrid controllers and smart meters exchanging commands and data, etc. The other is the electric
 grid. That is the electric wires that bring electricity to the customers and get electricity from the solar panel 
farms. Those are electric wires. The electrical system can continue to work without the data network. In fact, until a 
few years ago, that was all we had and it worked fine.
# @502 How are we doing participationwise?
- Question: I would be interested in knowing if I've been participating well in class and if my reading responses have 
the right amount of detail/words. I think others might also be interested as well since it's a graded component of the 
class- is there any way to be given some info about how we're doing participation-wise in the class so far?
- Tags: 
recitation
- Students' Answer: 
- Instructors' Answer: Yes! We do check-in grades every three weeks (see @280). You 
should've already received one on 2/25 (please reach out to your TA right away if you didn't!), and you'll get another 
one by the end of this week.  You can check the calendar for the dates these grades are released; they're all under 
"participation check-in #[1-3]".  If you're looking for more specific feedback -- as in, you got your check-in grade and
 want to improve -- reach out to your TA; they'll be in the best position to make individualized comments.
# @501 Change Matrix
- Question: When I tried submitting the Change Matrix, the system shows that "Keep in mind, this submission will count 
for everyone in your All DP Teams group." I just want to clarify, is the Change Matrix an individual assignment?
- Tags:
 design_project
- Students' Answer: 
- Instructors' Answer: First of all: remember that we're not grading the change 
matrix! We just want to see how you're using the impact framework.  Since the DPPR is a team assignment, we'd imagined 
that you'd do the change matrix collaboratively. But if not, feel free to just copy/paste multiple change matrices into 
one document and submit that.
# @500 Studying for the Exam
- Question: I am starting to get studying for the exam and I am struggling on how best to do so. The exam questions seem
 more technical/problem based versus in lecture and recitation I've been understanding things at a more high 
level.&nbsp;  Do you have any recommendations on how to best study or grasp solving technical problems on the exam? Is 
there a recommended way of studying?  Thank you!
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: Remember that
 the exam is open note! So you don't need to necessarily memorize any information, however I think it is helpful to know
 where to find it (what section in a paper etc).  When I took the class, I went back and went over papers and lectures 
that felt fuzzy to me so that I had a better overall understanding/it was more fresh. Therefore, when you get a question
 on it, even if you don't know the answer immediately, you can know where to look in the paper without having to scan 
the whole thing.  Additionally, if you took notes during recitation, reviewing those is definitely helpful as 
recitations tend to go over the more complicated details of a paper and take things that are abstract and make them more
 concrete.   Finally, practice exams are probably your best resource to get a sense of what the exam will look like.
# @499 What is a "stasis"?
- Question: This term is used frequently in tutorial and tutorial videos, but I don’t know what it means.
- Tags: 
tutorial
- Students' Answer: 
- Instructors' Answer: Stasis is a rhetorical concept that refers to a point of consent or
 dissent in an argument. Traditionally, these states of consensus occur along the lines of facts, definition, causation,
 evaluation, and policy. We've covered these five states in the videos and in a few different tutorials. 

For an 
argument to be effective, these five states need to be closed. In other words, you need to assure your audience that you
 and they agree on what the facts, definitions, causative chains, values, and outcomes of an argument will be. A key 
example in the DPPR are design properties. If you say that fault tolerance is vital to your design, you must define what
 fault tolerance means in this context (definition) and its causative impacts upon your design--or how it works 
(causation). You then must prove why its good for the design (evaluation) and prove it works. 

This goes back to hat 
day in my tutorial, but that might well confuse others on Piazza. Still, think about what facts are defined to determine
 that a categorical definition exists. What makes a hat a hat? What do we exclude from that definition in order to argue
 that something is a good X (hat/design choice/whatever)? How does whether something is a good X inform our argument for
 its use? Stasis is about ensuring these elements are accounted for in your reasoning chain.
# @498 No office hours 11am on Thursday
- Question: Hi all - Because of a conflict I need to cancel my office hours this week (11am on Thursday). There are lots
 of other hours available on Thursday though!
- Tags: logistics
- Students' Answer: 
- Instructors' Answer: 
# @497 Packet overhead
- Question: Do we have to consider the overhead of IP and Ethernet packet frame size when calculating how much data our 
transmissions between smart meter and micro grid controllers and also between microgrid controllers and the central 
servers use?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: It would be good to get a back-of-the-
envelop estimate of whether the headers are going to make a difference or not. But do not worry about perfection here.
# @496 TCP/UDP for smart meter and micro grid controllers?
- Question: In previous piazza questions it was mentioned we can choose to use TCP or UDP as part of our LTE 
transmission. Is this the case for both smart meters and micro grid controllers or just microgrid controllers?
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: For both of them.
# @495 Smart Meter Power Generated/Stored Information in One House
- Question: For the power stored and power generated records, assume one house has one solar panel installed, do the two
 smart meters installed in this single house give the same information about these?&nbsp;  Along the same line of 
thinking, when a house needs to share power/receive shared power, do we tell both meters, or just the meter in the right
 direction? (so out for share and in for receive)
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: 
Only one of the two meters at a house is connected to the solar panel system, so it is the only one that can learn 
anything about the power generated or stored. For the other meter, there will be no such records, because it has nothing
 to measure.  For a house to share, the meter that needs to be told is the one connected to the solar panel system.
# @494 Check previous questions first
- Question: Please read all the earlier piazza postings about the DP before asking a question. An increasing number of 
questions are repeats and with over 400 posts, I can't find the references for you. The more times I have to answer the 
same question, the less time I have to answer the new questions. Be kind to your classmates.
- Tags: design_project
- 
Students' Answer: 
- Instructors' Answer: 
# @493 Central Utility & Data
- Question: Does the central utility actually sends data, or do researchers/ management simply query the database?
- 
Tags: design_project
- Students' Answer: 
- Instructors' Answer: It could happen either way. That is not specified in 
the spec. That said, there are some situations in which the holder of data will only let researchers use the data at the
 holding site and not let it out, for privacy reasons.
# @492 Modifiers vs not on grades
- Question: How do we tell if an assignment does or doesn't have modifiers (i.e. what the max grade in an assignment 
is)?  (Rewriting here in case follow-ups on old messages are hard to see.)
- Tags: other
- Students' Answer: 
- 
Instructors' Answer: I'd recommend reaching out to the person who graded the specific assignment
# @491 Smart Meter "put" and "acknowledge"
- Question: In the case that a smart meter sends data to a microgrid controller and the microgrid controller isn't able 
to process it and send an ACK in time, what does the smart meter do? Does it keep trying to resend the data until it 
receives an ACK or does it just send the next interval of data after a certain amount of time?
- Tags: design_project
- 
Students' Answer: 
- Instructors' Answer: Yes, until the smart meter gets an acknowledgement for the data, it considers 
it not to have been received. Notice, that it is also possible that some of the data gets through, so the 
acknowledgement ACKs all the data that was actually received, so the sender may only need to send some of it again.
# @490 Smart Meter in Critical Services
- Question: Does the critical services microgrid only have 4 smart meters (one for each of the police station, hospital,
 fire station, and solar panel farm)? If so, does that mean power cannot be shared within this microgrid?
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: Yes it only has 4 meters. The solar panel farm power is 
already shared among them.
# @489 Diagrams from Lecture 13
- Question: I've added copies of the diagrams that I drew on the board today in lecture to the website, in case that's 
useful in reviewing the material.
- Tags: lecture
- Students' Answer: 
- Instructors' Answer: 
# @488 Central utility smart meter
- Question: Does the central utility have a smart meter built-in to it? Or do we need to use some other mechanism for 
the central utility to know that power is out. Also how does the central utility know how much power is in its battery?

- Tags: design_project
- Students' Answer: 
- Instructors' Answer: No, the central utility does not have a meter. But it
 is running the central utility power plant and electric plants for as long as they've been around can tell whether they
 have power or not. If the power plant isn't getting power, you can assume that it will tell the central utility 
computer that fact and you don't need to worry about how that happens. It's already in place.
# @487 Can the apartment building batteries be charged?
- Question: See above.
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: Each apartment building has a 
battery that can be charged by its respective solar panel.  Sort of. There are two kinds of batteries and I'm not sure 
which one you are talking about. Every smart meter and microgrid controller has a tiny rechargeable battery that will 
let it run for up to 48 hours. Those are completely rechargeable from the power on the wires. Separately in each 
apartment building there is one solar panel farm that includes big batteries. There is one for all 100 apartments in the
 building. That system can only be charged from the solar panels.
# @486 Detecting when we are disconnected from central utility
- Question: It says that during storm outages that we get disconnected from power lines. But how do we know when this 
happens? Is it up to us to design a method for detecting this?  
- Tags: design_project
- Students' Answer: 
- 
Instructors' Answer: No, you do not need to detect it. Basically, there will be no power on the line, so the house 
system will just know. There is no power to be had on that line. But, since the data network and electrical network are 
separate networks, if the data network is still up, the central utility will know if its power is down and can tell the 
microgrid controllers, which can tell the smart meters, if that is useful to you.
# @485 Battery state access
- Question: Does the microgrid controller have a continuous access to the battery state of all microgrid members 
connected to it? Or does it need to issue a get request to get the most recent state of a battery associated with a 
given smart meter?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: The history record for “power 
stored” is collected every 15 seconds by the smart meter. Assuming the homeowner has not decided to flip the switch that
 causes data to be pushed every minute, it would need a get request to obtain the data.
# @484 LTE Data limit
- Question: When we say each smart meter and micro grid controller has a 2 GB data limit, is that both for sending and 
receiving? E.g. if a smart meter sends 1 MB of data to its micro grid controller, does that 1 MB count against both 
devices’s limit?Also, if a packet gets dropped on the way, how does it affect or not affect this data limit?&nbsp;
- 
Tags: design_project
- Students' Answer: 
- Instructors' Answer: The amount is counted for each device. The customer is 
paying for their own service only.  If the packet leaves the network interface of the device it is counted. If it is 
dropped in the network, one doesn't get credit back.
# @483 Links for Lectures 13 and 14
- Question: Lecture 13 (halfway through the semester!): 
https://mit.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=c72fb9f8-e073-4827-867b-ae5600d68731 Lecture 14: 
https://mit.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=43075016-883e-46b9-9206-ae5600d6eca5  Slides will be posted 
before lecture so you can follow along!
- Tags: lecture
- Students' Answer: 
- Instructors' Answer: 
# @482 DP Prep WRAP Feedback
- Question: I was just wondering if it's expected to not have received feedback yet on our prep assignment. Thanks.
- 
Tags: design_project
- Students' Answer: 
- Instructors' Answer: If your feedback isn’t visible on Canvas, please reach 
out to your tutorial instructor right away.
# @481 When does a house use central utility power?
- Question: When does a house begin to use power from the central utility? Is it when the battery runs out, or when the 
battery is below its threshold?If a house uses central utility power when the battery is below the threshold, then what 
is the point of having the battery, if it is always kept above the threshold? Is it only to account for power outages?
-
 Tags: design_project
- Students' Answer: 
- Instructors' Answer: You've answered your own question. The house uses the 
utility power when it has no other power available, so its battery is essentially drained and there is no power being 
provided on the local loop.
# @480 Smart meter "Get" command
- Question: The description of the "Get" command for the smart meters says the following:"retrieve specified data from 
the receiver of the command, this may be to request all data or a subset of the data"How does this command work exactly?
 What does "specified data" mean? How does a microgrid controller specify what data it wishes to receive? I understand 
that we are not allowed to decide how the smart meters are programmed, so what subsets of data may the microgrid 
controller request from the smart meters?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: Yes, the 
get command allows the microgrid controller to ask for a particular type of record and number of records. There are a 
variety of reasons this might be important, but if it isn't in your design, then specify that you will always get 
everything that is available.
# @479 What is the purpose of the put command?
- Question:  In the DP Spec, it lists the get command, which can be sent from the microgrid controllers to the smart 
meters to get data from them. Given that the get command exists and the smart meters are apparently not programmable, 
when is the put command ever run, and for what purpose?
- Tags: design_project
- Students' Answer: 
- Instructors' 
Answer: In the real meters (and in the protocol spec) the microgrid controllers may also send data to the smart meters. 
Apparently, they can send things like the current electricity prices. Those must be much smarter smart meters. So, for 
completeness it is there.
# @478 Smart meter threshold communication
- Question: Is there any way for the microgrid controller to figure out what thresholds their corresponding smart meters
 are using (i.e., whether they are set at 75%, 50%, or 25%)? If not, how does the microgrid controller know that any 
battery is below its threshold?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: See #1 in @446
# @477 Smart meters sharing power
- Question: Do the smart meters automatically send power back to the central utility when they are full and power 
sharing is off?Also, when power sharing is on, how do the meters know which neighbor they should send the excess power 
to?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: Does @445 help? If power sharing is on, the power
 is then available on the local power lines for whichever neighbor who needs it to use. If power sharing is turned off, 
excess power is sent to the central utility.
# @476 Reward for Sharing Power?
- Question: What reward would someone actually gain for setting their min-sharing threshold to be lower? The spec says 
that only power that is shared outside of the grid is discounted on the bill, and power can only be shared outside of 
the grid once a home’s charge has reached maximum capacity (p. 6). So, for example, consider a microgrid with just two 
homes. If Home A has set their sharing capacity to 75% and Home B sets their capacity to 25% and both are initialized to
 50% charge, then B would share its excess charge with A until both A and B reached their respective thresholds. 
Assuming both homes charge at the same rate, then Home A would be reach 100% before Home B, which would allow it to 
start sharing power outside of the microgrid sooner and receive more of a discount while having done less overall 
sharing than Home B. Is this the intended design for the system or am I misunderstanding it?
- Tags: design_project
- 
Students' Answer: 
- Instructors' Answer: Let's take this apart a bit. First, a house will start sharing into the local 
loop if asked and only as long as it is above its own threshold. Once it reaches that threshold it will stop, so the 
house receiving the power will have to go to the central utility's power.   Now, if a house sets its threshold to 75%, 
it will only share anywhere if its power is above 75%, so it might keep more in the case where it is asked to share with
 the local loop, but it will also only start sharing and getting credit when its battery is over 75%. It can get more 
credit if it sets its threshold to 50%, but also may be called on more often to share with the local loop.  (BTW, this 
is a repeat of several previous postings.)
# @475 Lossless aggregation behavior
- Question: Hi! I am having a bit of trouble understanding lossless aggregation, specifically, whether there is any 
reason at all to prefer non-aggregated data over lossless aggregated data. After all, lossless aggregation does not 
result in any loss of information, it reduces space needed for storing data and network bandwidth usage, and in general 
seems to make things more efficient. Why is this provided as a choice at all? Is there something I am overlooking?
- 
Tags: design_project
- Students' Answer: 
- Instructors' Answer: It is included because that is the simplest, most basic
 model. The aggregation was added later as an option. That said, it is your choice as to when and how to use it.
# @474 Word count - appendix and assumptions
- Question: If we have an appendix that details assumptions and calculations to support our choice of numbers throughout
 the design, can we exclude these from the word count as appendices in papers are often excluded from page counts?
- 
Tags: design_project
- Students' Answer: 
- Instructors' Answer: If you go significantly beyond the word count, you can 
expect that the reader may just not read the extra material. It won't be "counted" in what is focused on for reading.  
In some cases, when writing there are just hard limits and everything counts. In others not. In this case, it is 
definitely more important that you do a good solid job on the part that will be read.
# @473 Fairness concerns for DP
- Question: I was curious about a situation where one home in a microgrid uses much more power than the other homes, so 
that it would be unfair to require the other homes to provide that home with power for free (rather than being able to 
send their excess power back to the central utility for credit), but it would still increase total happiness for that 
home to be provided with power. It seems that there are some circumstances, such as this, where the house receiving 
power should have to pay their neighbors to share their power.However, the spec states that "there is no accounting that
 appears on monthly bills for [power sharing]." I'm confused about why this seems to suggest that we don't have the 
option to have the power sharing affect residents' power bills. Would it be allowed (within the spec) for our system 
design to include a component where customers may be charged or rebated based on their power sharing within the 
microgrid? (Assuming that the system would still be compatible with the physical constraints of the system.)
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: Yes, the town picked a simple and imperfect solution. As I 
think I've mentioned in several other piazza posts (can't find them right now), it is assumed that neighbors kind of 
know each other and are less likely to land on their neighbors unfairly than with people they don't know, but there is 
definitely an opportunity for unfairness in exchange for simplicity.
# @472 Regional Grid Prices
- Question: Does the central utility know how much the New England regional grid is going to charge for electricity at 
each time of the current day, or do they only know the price at that particular moment in time?
- Tags: design_project
-
 Students' Answer: 
- Instructors' Answer: You van assume that the rates are set monthly with enough advance to plan 
ahead.
# @471 How to think about prioritization edge cases?
- Question: It seems like there are quite a few different edge cases in which we might need to start prioritizing power 
(ie. the New England power grid goes down, the CMLC power plant goes down, the New England power grid starts restricting
 the amount we can purchase, etc).  How should we go about thinking through the responses to all these cases? Should our
 system always ensure that town services have 75% battery before trying to serve apartments/houses, even if that means 
letting lots of people go without electricity?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: Yes, 
it is a complicated system with lots of ways to not work as you might hope. One way to think about designing complex 
systems is to begin with making sure that your system is appropriate for the most common case(s). You can then add more 
complexity as time permits and as you think appropriate. There may be some situations for which you decide there is no 
good solution. Primarily, you want to be clear about what your system does and does not do.  That all said, it should 
address the use cases in the spec.
# @470 Utilities Microgrid Battery
- Question: In the spec, the house and apartment microgrids have a 24-hour battery associated with them. Does the solar 
panel associated with the utilities have a 24-hour battery as well?
- Tags: design_project
- Students' Answer: resolved:
 "The central utility and each location of solar
panels has a system of batteries."
- Instructors' Answer: 
# @469 how much storage does the central utility have?
- Question: The errata says 1TB but the spec says 2TB on page 10. Are we meant to store data for 5 years on the central 
server for long-term planning and is this feasible?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: 
Sorry. That was a typo on my part, 2TB.  That said, since the town would like to have the data for 5 years, it would be 
a good idea to do that, if possible. If it's not possible, explain.
# @468 Purchasing power
- Question: Having read some posts on piazza, I think our team is very confused how purchasing power works. We got an 
impression that houses (or apartments or critical services buildings) will "buy power" automatically (i.e. if we don't 
have power on a local microgrid or we don't have any power in our battery then we just automatically ask utilities to 
give us power to continue operating). On the other hand, we saw some posts on piazza suggesting that it would be a good 
idea for central utility to purchase power in off-peak hours and store it in their batteries. This made us think that it
 would be possible to design some system which would force central utility to purchase power (say following some rules 
we design). Does it mean that central utility battery can purchase energy "in advance", unlike houses? Can we design 
some system that would force central utility to purchase power in advance to lower the process for the town? Or does it 
only purchase power automatically if its battery goes below the threshold decided by the town? Thank you!
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: You are correct in your understanding. The houses will 
automatically get power from the CMLC (at the current rate), if they do not have other sources for power.  For the 
central utility itself, it will provide power bought by its customers from its batteries, assuming it has any. It can 
also charge up its batteries at any time that it is low, from the regional utility. It would make most sense for it to 
do this during off-peak hours, if possible. You get to design this scheme at the central utility, but you do not need to
 design the electrical system that will carry this out, only the control system that will decide when and how to 
optimize buying electricity from the regional utility.
# @467 "Some additional questions from the town"
- Question: Do we need to address this section in the DPPR?
- Tags: design_project
- Students' Answer: 
- Instructors' 
Answer: I don't see where you found this. It is not in the DP Preliminary Report assignment, as far as I can tell.  I 
will get back to this shortly with a more complete answer.
# @466 Sunday Night OH Cancelled 3/13
- Question: Hi all, tonight's OH from 8-10 will be cancelled - feel free to reach out to me directly if you were 
planning on coming/have a question, and we can schedule something. My email is kjain21@mit.edu. Sorry about the late 
notice!
- Tags: logistics
- Students' Answer: 
- Instructors' Answer: 
# @465 Battery CMLC and central utility
- Question: Our team is a bit confused about the difference between central utility power management and CMLC. The 
diagram in the spec doesn't show any power line between central utility and the microgrid, only between CMLC and the 
microgrids. On the other hand, the spec mentions that "the central utility and each location of solar panels has a 
system of batteries". Does central utility store power? Or does the storage happen only on CMLC side? If microgrids sell
 power, does it go to the storage in CMLC or to the central utility battery, or are these two equivalent? In addition, 
"If the town batteries fall below a minimum set by the town, they will buy extra power from the New England regional 
grid." - which batteries does this sentence refer to - CMLC or central utility? Thank you!
- Tags: design_project
- 
Students' Answer: 
- Instructors' Answer: I'm sorry that this is confusing. The CMLC is a company that owns and runs 
both the central computing facility and the whole town power plant (including those central batteries and all the power 
lines and poles in the town, plus any other equipment needed to run the electrical system of the town).   The only 
batteries that can be refilled with power from power lines are the batteries owned and operated by the CMLC. That power 
can come from the individual solar panel systems, in which case the meter on each of those systems will record how much 
power each system provided to the CMLC batteries or from the power lines from the regional utility. For any power 
provided to the central battery system by a customer, that customer will receive credit on their bill - so, in that 
sense the town is paying the customers for their excess power. If power comes into those central batteries from the 
regional utility, the CMLC will be paying the regional utility for that power at whatever the current rate is You are 
right that if the CMLC batteries fall below some threshold, the CMLC will buy power from the regional utility to boost 
its batteries.
# @464 Apartment building batteries
- Question: If there is only one smart meter to measure outgoing power, can the apartment batteries be charged via 
microgrid sharing/purchasing from the central utility or will that energy go directly to the apartments that use it? If 
so, how will we track this information?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: There is no 
way for power to go from the utility lines into the apartment building battery system. The only source of power those 
batteries have is the solar panels, just as with the other solar panel systems.
# @463 Networking Question
- Question: Since each device has their own static IP address, can every device directly communicate with every other 
device over internet? E.g: Could the central utility directly send messages to smart meters without passing it through a
 microgrid controller? Can microgrid controllers directly send messages to each other without passing it through the 
central utility? If this is the case, also what makes a microgrid controller belong to a specific microgrid, since every
 microgrid controller can directly communicate with every smart meter? Thanks.
- Tags: design_project
- Students' 
Answer: 
- Instructors' Answer: Technically, in terms of sending IP traffic, yes, they can send something to any other 
IP address. That said, the design is constrained so the smart meters only communicate with their own microgrid 
controller. Each microgrid controller only communicates with the meters in its microgrid and the central utility and the
 central utility only communicates with the microgrid controllers.  Just as an aside, if you are building an IoT system,
 say a home alarm or power management system, you typically really want to limit those devices so they only can 
communicate with a very circumscribed set of other devices. As we will see later in the term when we read about the 
Mirai attack, constraining destination IP addresses is definitely a way to reduce denial-of-service attacks (and other 
kinds of attacks). But, this is way beyond what you are doing now. But, one would try to design a system with 
constrained communications paths, for very good reasons.
# @461 Size of data fields
- Question: Are we allowed to alter the size of fields for history and event logs? For example, why do we need 64 bits 
for meter ID if we only have few thousand smart meters and why do we need 8 bits for record type if there are only four 
record types?&nbsp;
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: No, you can't alter them. You 
cannot change the programming of the smart meters.
# @459 Confusion about battery threshold and sharing power
- Question: Does each battery know when it is above its threshold and is able to share power with either the central 
utility or the local loop? For example, if the share_power_on command is sent to a smart meter on a battery below its 
threshold, does the battery know not to share power within the microgrid?
- Tags: design_project
- Students' Answer: 
- 
Instructors' Answer: A battery knows about its own battery level with respect to its own threshold. What it doesn't know
 is anything about any of the other batteries in its microgrid. Only the microgrid controller knows these facts about 
all the systems within the microgrid itself.
# @458 share_power_on when no one needs power
- Question: Consider the case when every house in a residential microgrid is generating more power than it needs, is 
above its battery threshold, and is instructed with share_power_on. As no house in the microgrid actually needs the 
power, does it just get wasted, does it go to charging batteries, or does it go to central utility? What about when all 
but one house is above its battery threshold? More generally, would a house instructed to share power ever send power 
back to central?
- Tags: design_project
- Students' Answer: If every house in a residential microgrid is above its 
threshold, then they shouldn't be instructed with share_power_on since, as you note, the power would be wasted. Instead,
 it's recommended that the share_power_on instruction is sent only when a house is above the threshold and another house
 in the microgrid is below the threshold.  Deciding the optimal way to apply the share_power_on instructions is up to 
you in this case. There are multiple ways to approach this, each with its own pros and cons (share equally, share based 
on percent over threshold, etc.).  No,  if a house is sharing power, it's assumed that another house is below threshold.
 However, sending power back to central assumes all houses are above threshold (and the house sending power back is at 
max capacity). .  
- Instructors' Answer: 
# @457 @303 vs @403
- Question: these two answers have contradictory information. One says that "power from the town can be used to charge 
batteries, and it is a really good idea to do this, if needed, during non-peak hours." The other says that the only way 
to "the only way a battery can gain electricity is from its solar panels."&nbsp;  All in all, the whole process of what 
happens above the threshold, both in terms of sharing excess and buying power, is a bit hazy. The process is said to be 
automatic but is there a way to actually have control over buying in excess and not sharing our excess?  We want to have
 this control over electricity distribution for our design to optimize for both the normal and extreme cases.&nbsp;
- 
Tags: design_project
- Students' Answer: i think it might be two different batteries here. power from the town can be 
used to charge batteries [of the central utility], and the only way a battery [connected to a solar panel] can gain 
electricity is from its solar panels? ________________________________________________ not the answer we were looking 
for--> @303 asks specifically about charging resident batteries with power from the town to which the answer was yes, so
 in any case Not Resolved
- Instructors' Answer: Yes, there are various batteries here. The batteries associated with a 
solar panel system can only be replenished from the solar panel system itself. The batteries in the central utility can 
be (must be) replenished from power lines, either those coming back from the electric customers in the town or from the 
regional utility.  Finally, there as a bit of confusion about some very small batteries provided as backup for the smart
 meters and microgrid controllers. These allow those devices to continue operating for up to 48 hours without power on 
the lines, just in case. These are so limited that they are not a resource for a house, apartment or emergency services 
building. Think of them like the batteries in a smoke detector system. They are recharged from the power lines, when 
there is power available and really just allow some of the components to keep operating under emergency conditions.
# @456 Charging batteries through power from central utility
- Question: is there a way to "force" houses to buy power from the central utility above their minimum threshold? For 
example, we were thinking if we see that we are in the storm outage use case and the data network is out, we want houses
 to take from the central utility to a certain point above their threshold so that we can ensure they won't be without 
power for the duration of the storm. Is that possible?
- Tags: design_project
- Students' Answer: 
- Instructors' 
Answer: There really isn't a way to do this as the system stands. It might be a good idea, so you can certainly include 
recommendations that would improve the system.
# @455 Problems with Central Utility
- Question: Does central utility need to calcualte billings?&nbsp;
- Tags: design_project
- Students' Answer: 
- 
Instructors' Answer: See @440
# @454 Un-Isolate
- Question: The ANSI 12 protocol has an Isolate command, however I see no Unisolate command. How should one go about 
reversing an isolate command?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: See @431
# @453 Extreme demand use case/battery charging rates
- Question: I'm a bit confused about how to handle the extreme demand use case. I saw on piazza post @360 that the solar
 panel farm can provide 100% of average for 24 hours for the municipal buildings, does this mean that the solar panel 
farm is at 100% capacity during the normal use case? I'm just confused about whether or not the solar panel farm can 
generate enough electricity for the municipal buildings during the extreme demand use case.  Also, for the subsidized 
housing buildings, the normal use case says that the solar panels are generating "enough" power. But for the extreme 
demand case, does this mean they're not generating enough?  Am I just thinking about this too much? Should we be 
designing for many situations? I can think about a situation when maybe the subsidized housing is not generating enough 
power, but the central utility is generating enough power because maybe the residential and municipal buildings are 
generating enough power to give to the central utility. I feel like there's a lot of variables to consider, and I'm just
 confused if we're supposed to know about these or we're supposed to design for many possible situations.
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: All the solar panel systems have the same design requirement 
- that they have enough panels so that with enough sunshine they can generate 100% of the average use of their 
customers. So, for the emergency services buildings, the solar panel farm will be designed (not by you, but by the 
company providing the equipment) to meet that requirement. Notice that this is all average. The "normal" use case may 
not be average, but it is not a crisis or exceptional case. It is within the bounds of normal behavior that the system 
can expect.  With respect to the apartment buildings, yes, if the system is designed to provide enough only enough power
 for normal use, then under circumstances of abnormal demand, the system will not be able to keep up.  Yes, there are a 
lot of things to consider in your design. You want it to be as flexible and adaptable as you can, but it will never be 
perfect and will never be able to provide for all circumstances, so you need to think about the conditions under it will
 and won't work and just justify your design point with respect to that.
# @452 Microgrid Controllers Processing Capabilities
- Question: How many cores and/or RAM do the microgrid controllers have? I'm wondering because this could affect the 
type and structure of the computation we perform on the microgrid controllers.&nbsp;
- Tags: design_project
- Students' 
Answer: 
- Instructors' Answer: Start with @405.   But to follow up on that, it has a single processor (unlike the 
central utility).
# @451 Smart Meter Storage
- Question: Are we supposed to design the storage system for the smart meters? In other words, determine how exactly the
 history and event logs are separated/organized in memory? Or can we assume that that functionality has already been 
taken care of by the smart meters? I am a bit confused because the smart meters are not programmable so I am not sure 
what changes/additions we as designers can possibly make to them.
- Tags: design_project
- Students' Answer: 
- 
Instructors' Answer: The functionality of the smart meters is outside of your control. That said, if the smart meter is 
in the non-automatic sending mode, you might want to think about whether the frequency of pulling data (and therefore 
having it deleted from the smart meter) is an issue.
# @450 Even Log Records
- Question: Do those records indicate a change of the smart meter mode from power-sharing mode on/off?  Is that what the
 spec refers to by: ": running disconnected from the power net, running on the power net"
- Tags: design_project
- 
Students' Answer: 
- Instructors' Answer: Yes.
# @449 Central Server Specs
- Question: The DP Spec states that the central server has an 8-core 2.6 GHz Intel processor. Are we expected to use 
those numbers in our calculations? Because I don't know how to incorporate the number of cores or the clock speed into 
the design.
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: Only if they are useful to you. If you 
happen to have designed something that can take advantage of 8 processors working in parallel then this fact might be 
useful. If that is irrelevant to your design, then it is not useful.
# @448 Smart meters sharing power
- Question: I see that the smart meters now have "Share_power_on" and "Share_power_off" commands. But it seems like 
these commands simply notify the meters that power sharing should occur or should not occur. Is there a part of the 
smart meter API that allows us to tell a specific house to send power to a specific other house? Or is that part 
automatic somehow?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: I;m a little confused. A command 
will be directed to a particular smart meter, the one with the IP address specified. There is no broadcast or multicast 
here. Each instruction must have a specific destination. That is the meter that will receive any particular 
share_power_on or share_power_off command.
# @447 Lossless Aggregation Message Size
- Question: I am unsure how to calculate the amount of data that would be used a message of lossless aggregation. Does 
it only use every field once and just include more data in which case it would use 36 + 8*(aggregation_length - 1), or 
does it send a start and end time for each individual measurement as well?
- Tags: design_project
- Students' Answer: 
-
 Instructors' Answer: A record reporting something like amount of power through the meter or amount of power generated 
or stored has only a few fields. Notice that each one has a value for the reading and a start time and end time. 
Lossless aggregation can only occur if the value over more than one reading is identical. At that point the consolidated
 record will have the start time of the earliest record and the end time of the latest record and the value of all of 
them. This record is no larger than any of the original individual records were, but there will be fewer of them.
# @446 Two missing things missing from the spec.
- Question: There are two things that were overlooked in the spec.  1. When a smart meter is initialized, the spec 
indicates that the initialize command will be acknowledged and that all acknowledgements can carry information. When 
acknowledging initialization, two things at least will be included, whether or not the smart meter is set to send its 
data automatically or not and what its battery threshold is, if it is a smart meter attached to a solar panel system.  
2. As it stands there is no way to manage a serious power shortage when either of two things might be desired. The first
 thing that might be useful is for a smart meter to be notified or a shortage, so that it can alert the customer to 
reduce their power demand. This may be initiated originally from the central utility reporting to the microgrid 
controller (where you are designing the system), but the spec does not include any way for a microgrid controller to 
report anything like this to the smart meter. You will need two more smart meter command for 
this:&nbsp;reduce_power_demand_on and&nbsp;reduce_power_demand_off.&nbsp;  The second is that there is no way for the 
central utility to give priority to one microgrid over another, especially the emergency services microgrid. In fact, 
utilities can do this, but it was not described in the spec. They can either reduce or turn off the power to parts of 
their systems. Your central utility will need to figure out when to do this, but you can assume that once the decision 
is made, the central power plant can be instructed to carry this out. If it involves reducing or turning off the power 
to some of the other microgrids, you may want the central utility to inform the microgrid controllers involved.
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: 
# @445 Brief answers to a small number of common questions
- Question: It has come to my attention, not only through piazza but also as reports from some of the teaching staff, 
that would be useful to summarize answers to a few common questions. There is lots more detail about these topics in 
previous piazza questions and answers.  1. Power on the lines is just there or not. You cannot route power to a 
particular customer. A house's local power system will choose power from one of three options. It's first choice is its 
own batteries. If they run out, then if one or another house in the microgrid has been instructed to share its excess 
power, the original house will choose to use that power. (It's free.) If that is not available it will use the central 
utility power. The contract with the central utility is that it will provide power. This only doesn't work when there is
 a power failure (as in one of the use cases).  2. The amount of electricity that a customer's system can use is defined
 by its ampere service. So each house can use no more than 200 amps and each apartment no more than 100 amps. This is 
unrelated to the source of that power. That is what their wiring systems are designed to handle.  3. The decision about 
whether a house is sharing on the local loop or not is made by the local microgrid controller. It must notice that the 
local solar system batteries of a house are low and dropping (an indication of power usage in the house). It will also 
know the battery levels of all the other houses in the microgrid and, for any over their thresholds, they will be 
instructed to share on the local loop, which has the side effect of their no longer sharing with the central utility. 
This is done by the microgrid controller sending a share_power_on instruction to the smart meter of any house that will 
be sharing. Then the house that will be in need of additional power can get it from the local loop as needed. Once 
things stabilize again (for example, the battery levels of the original house might be rising), the microgrid controller
 will then turn of sharing by sending share_power_off to each smart meter that had previous been instructed to share. 
Those houses will then return to sharing with the central utility as they have power available for that.  As I said, 
these are only highlights. There is much more detail in previous piazza postings.
- Tags: design_project
- Students' 
Answer: 
- Instructors' Answer: 
# @444 Regrade Requests
- Question: Can we regrade request a hands on?
- Tags: handson2
- Students' Answer: 
- Instructors' Answer: Yep! Sorry 
about that; I didn't realize Gradescope wasn't turning them on by default.
# @443 Lossy Aggregation with less than 10 Records
- Question: If the smart meter is asked to run lossy aggregation and there are less than 10 data records, does the 
algorithm still work? That is, would it pad the data somehow or would it just just average whatever records are there 
appropriately?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: It won't send a less than complete 
record. It will just wait. Since the measurements happen every 15 seconds, once one is using the lossy aggregation 
model, there will only be records available every 150 seconds, so on some 1 minute boundaries there may be no data to 
send. The point of aggregation is to send a reduced amount of information.
# @442 What happens if one member of a group drops the class?
- Question: 
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: We turn you into a team of two! We have 
contingency plans for this (we end up with a few teams of two every year). We typically reach out once we get the news 
that a student has dropped the class, but sometimes their teammates find out earlier than we do (e.g., their third 
teammate announces they're dropping but doesn't fill out a drop form immediately). If you're in that case, email me 
(lacurts@mit.edu).
# @441 How do we control whether or not e.g. residence smart meters are drawing power from the local loop?
- Question: 
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: You don't need to. If a house needs 
power beyond what its solar panel system can provide, it will automatically try the local loop. If there isn't power 
there, it will automatically use power from the central utility. Part of the central utility's contract is that it will 
always have power (unless there is a power failure, as in one of the use cases).
# @440 Central Utility Questions - different modes of operation, data storage
- Question: 1. (referencing question @424) In Section 2.2.3 the central utility is described as “locus of decisions” for
 quite a few things, including billing, when to buy power from the New England grid, long-term planning, and when to 
prioritize certain buildings. How much of this does our system design need to deal with? For billing and deciding when 
to buy power, is it sufficient for us to make sure central utility stores usage data so that another system can figure 
out billing and modeling usage? Moreover, the spec says that management wants monthly, quarterly, annual, and 5-year 
rolling period information about usage patterns. Does this mean our system has to deal with calculating any information,
 or is it sufficient to make sure central utility has this information? Do we have to store 5 years’ worth of 
information, or can we assume the management team will extract past data to store somewhere else? 2. How often will the 
MIT researchers be collecting their fine-grained data? Can we assume that the utility management team will be collecting
 their data at the monthly, quarterly, annually, and 5 year intervals? Or do we tell them when to collect?
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: 1. Yes, the central utility has to do a lot. You do not need 
to design the billing or behavior modeling components, but you need to recognize that they will be happening 
concurrently with anything else the central utility is doing. Yes, you will need to store the data. There is nowhere 
else for it to be stored. These are the resources the town has.  2. The MIT researchers will be accessing the data 
infrequently. Perhaps every few months. It is undecided as yet whether they can make a copy of the data to use elsewhere
 or must only use it on this system. Often municipalities will only let analysis happen on their own machines, and not 
let the raw data out for privacy reasons.
# @439 Microgrid / Smart Meter Questions - power sharing, drawing from neighbors vs. central utility
- Question: 1. Do the smart meters connected to solar panels track how much power is shared within the microgrid local 
loop, in addition to the power shared with central utility? (It has to be able to differentiate between these for 
billing purposes, right?) Also, we know that we use the Share_power_on/off commands to share power within the microgrid,
 but how does the microgrid controller instruct smart meters to start giving power back to the grid? Do we even control 
it? This is unclear given the response to @387. 2. Are the microgrid controller’s smart meters the only ones that 
measure power in and out between the microgrid and central utility? Or do the individual buildings smart meters do that 
as well? Put another way, how are the smart meters on buildings/houses connected? (between solar panels + battery, solar
 panels + microgrid, solar panels + microgrid and central utility grid). 3. Does a house only draw power from its 
neighbors (through the local loop) when its own batteries are empty, or will it default to drawing power from its 
neighbors when its batteries are below the threshold (therefore allowing its own batteries to charge)?
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: 1. The smart meter on the solar panel system records three 
types of data, the amount generated, the amount stored in the battery, and the amount that passes through the smart 
meter on its way back to the central utility. It can send power to three places all told, the central utility, the house
 itself and the local microgrid loop. It does not distinguish these last two. If you find that it is important to do so,
 you should propose a change to what the smart meters do with a justification for it, but it is unlikely that such a 
change can be made, because those are bought off the shelf, as is.  2. Every smart meter measures the electricity that 
goes through it. These meters are used in two ways. The first is that every customer has a smart meter that measures the
 amount of electricity the customer draws from the central utility. The second is that every solar panel system has a 
smart meter. The power that goes through it is the power it is sending back to the central utility. That is the complete
 set of smart meters in the system.  3. You are designing the microgrid system, which decides when power is made 
available on the local loop. So, you can decide this. But, in general, a house will use its own batteries until they are
 essentially empty because that is both free and most reliable. If its batteries are essentially empty, its second 
choice is the local loop, if the microgrid controller has found at least one other house that has available power to 
share on the local loop. If that fails, the house will switch to the central utility power.
# @438 Preliminary Report Word Count
- Question: I was wondering how much over the word count we could go on the DPPR. Is it ~10% like on the prep 
assignment?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: That's a good guideline.  The main thing 
to remember about the word count is that we're using it to help you understand the level of detail we're looking for, 
not because we're planning to actually count your individual words. If you write much more than the given word count, 
you're giving us too much detail; much less, not enough detail.
# @437 Exam 1 Location
- Question: I know the location for exam 1 is currently TBD according to the website, but I'm assuming that the test 
will be 100% in-person, correct?&nbsp;
- Tags: exam1
- Students' Answer: 
- Instructors' Answer: Yep, it'll be in 
person. We'll know a location once room reservations go through.
# @436 Power control
- Question: At first, our team believed that one of the main goals of our system is power routing, but after looking at 
discussions in @424 and some other Piazza posts, it seems not to be the case. I'd like to clarify how power flow is 
controlled.  1. Does our designed system have to control the power flow/power routing (besides telling smart meters 
share_power_on or share_power_off)? 2. Is our designed system even able to control the power flow besides telling smart 
meters share_power_on or share_power_off?  Based on the Piazza discussions, it seems the answer is no to both questions,
 although I am not sure. As I understand, a building will automatically sell power to town if its battery level is 100% 
and automatically buy power from town if its battery level is (close to) 0%.  There is also a follow-up question on @424
 that if we cannot control the power, how would the goal "If there is significantly high demand for power and reduced 
availability from the external grid, the utility will give highest priority to the microgrid for the hospital, and 
police and fire stations." be achieved. Is this prioritization something that we are responsible for, or is it done 
automatically?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: The share_power_on and share_power_off
 are actually important, because they save people within a microgrid money. As a secondary effect, they also do cost the
 sharer something potentially, because at those times the sharer is not getting credit on their bill.  So, this is 
exactly a control of the flow of electricity that might be stored in the local batteries.  You're last question is a 
good one. Although the town might like this to be a goal, it seems like it may not be feasible with the capabilities 
you've been given. What would you need in order to be able to achieve this?
# @435 Clarification of DPPR grading
- Question: We heard some confusion from a few students this week, so I wanted to clear this up: your DP preliminary 
reports are read by both your recitation instructor and WRAP instructor, but you will only receive a grade from your 
WRAP instructor (see here).  Your recitation instructor will give you feedback on your design, which you should 
incorporate into future deliverables. But you're not graded on your actual design at this stage.
- Tags: design_project

- Students' Answer: 
- Instructors' Answer: 
# @434 Impact Framework Example
- Question: We've designed the Impact Framework for you to use as a tool through your Design Project. In response to 
what we're seeing on the DP Prep assignment, and in expectation of the upcoming Preliminary Reports, we've created an 
example of how you might use the framework (it's linked to on the design project page). Please take a look! It should be
 useful as you work on your Preliminary Report.
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: 
# @433 Special OHs for design project questions?
- Question: Hi! This is more a thought than a question. I was wondering if it will be possible to have special office 
hours with the authors of the design project to answer clarifying questions. There are a lot of repeat questions on 
Piazza and it must be difficult to keep up with them all. Maybe this could be a way to scale answering questions?
- 
Tags: design_project
- Students' Answer: 
- Instructors' Answer: I'm curious about this (but open to the idea!). In 
theory, Piazza is the way we scale these questions. All of you can see the responses (unless you're posting privately), 
so our hope is that students will search/skim through previous questions before asking new ones. Piazza also gives us a 
chance to think through questions that hadn't occurred to us during development of the spec (sometimes we realize we 
just need to clarify a point, other times we realize we need to specify something that is currently un-specified).
# @432 Central Utility power routing
- Question: Can the central utility route power to a specific house, or does it route to the microgrid, at which point 
the microgrid controller decides how to distribute it? Or, is the power arbitrarily distributed amongst the houses of a 
given microgrid and then re-routed by the microgrid controller? Does the answer to either question change if the house 
requests power in the first place?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: I know I've 
answered this before, but I can't find it right now, so it is quicker just to answer again.  The central utility is 
always making power available on its wires to any building or apartment that needs it at any time under normal 
operations. It doesn't need to direct power anywhere, it is just always there to be used as needed (and metered if it is
 used). So, if a house is short of electricity, there are two paths by which it can get power. If there is one or more 
other houses in its microgrid that have more than their threshold setting, the microgrid controller can instruct those 
houses to provide excess into the local loop. Notice that this is done outside the metering, so the house that is short 
will not pay for this. So, this is a preferable source. But if that doesn't happen (there is no power available on the 
local loop) it will automatically use power from the central utility power line, for which it will pay at whatever rate 
is applicable at that time. 
# @431 Confusion about the Isolate instruction
- Question: I read @383 and I'm still a bit confused about what the isolate instruction actually does. I assume that if 
the central utility goes down, the nodes in a microgrid need to share power amongst each other. However, isn't that what
 the default functionality is supposed to be? In isolation mode, are all the nodes supposed to share power equally, even
 if one node has their minimum at 75% and another at 25% so that one house doesn't lose power before the others? Is that
 a design decision we're supposed to make?  Also do microgrid controllers and meters need a way to de-isolate?
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: I've added more to the answer to @383, but let me pick up 
here as well.  The isolate "command" is informative, but not necessary.   But you are making an assumption here. 
"Normal" operation is to provide any excess power in the battery above the threshold back to the central utility. 
Providing power into the microgrid local loop is exceptional. Just because the central utility is inaccessible from the 
"electricity" perspective does not mean that sharing within the local loop will be happening. It will only happen if the
 microgrid controller discovers that one or more houses are below their threshold capacity in their batteries. If they 
are all above, the houses will operate independently.
# @430 Office Hours- Thu. 8-9 in 34-303?
- Question: Are there office hours right now? I went to the room and there’s another class in there
- Tags: logistics
- 
Students' Answer: 
- Instructors' Answer: 
# @429 At what rate do houses supply power to the central utility?
- Question: (Unresolved followup to @352) What is the (maximum) rate at which a house can supply power to the central 
utiility, ideally measured in battery percentage / second (e.g., 1% / second)? When all batteries in a micogrid are 
full, the microgrid controller should instruct them to send power to the central utility to avoid waste. However, the 
central utility battery is much larger than the batteries of each individual house (or even microgrid). If there is no 
mechanism for a microgrid controller to limit the rate at which it supplies power to central utility, the central 
utility would very quickly drain all of the energy stored in the microgrid, leaving the houses’s batteries empty. As the
 DP spec provides no way of specifying the rate at of supplying power (just Share_power_on and Share_power_off), the 
microgrid controller needs to have an estimate of the maximum rate so that it can know how often to poll the battery 
smart meters for their charge and to consider updating their sharing state. For example, suppose the microgrid 
controller wants to send 5% of battery energy to the central utility. If the maximum rate is on the order 1% / s, the 
controller would probably want to poll the batteries every couple of seconds. On the other hand, if the rate is on the 
order of 0.01% / s, it should poll about every minute to avoid wasting bandwidth.
- Tags: design_project
- Students' 
Answer: 
- Instructors' Answer: Let me take your questions one at a time.  1. There is a maximum rate at which power 
will flow through a copper wire. If you believe that is important, I have no doubt that information is available, but 
you will need to think about why you need to know this.  2.  A battery system will only provide power to the central 
utility until it is reduced to its threshold. If the threshold is reached it will stop, unless its solar panels generate
 more. The central system will never drain the local batteries, but only draw them down to their thresholds. In 
addition, this is the normal behavior mode, the local batteries will be sharing excess with the central utility. It is 
only in exceptional cases that the local system will switch to providing its excess power to the local microgrid loop, 
and that only for as long as needed.  3. The amount of power in a battery is recorded every 15 seconds. See p. 7.  4. 
The rates at which measurements are taken and sent are predetermined, except in the case where the homeowner has set a 
meter not to send its data automatically. In that case, you will need to design the microgrid controller with a schedule
 for when it will request which data. In both cases, you will want to understand what the load will be on the network 
and receiving microgrid controller.
# @428 Share_power_on
- Question: If we want a smart meter to receive power from the microgrid but not to send power, do we tell it to 
share_power_on or share_power_off?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: I’m a little 
confused about what you are asking. The smart meter isn't commanded to receive power from the microgrid. A 
share_power_on command will be sent from the microgrid controller to a smart meter that has excess power in its 
batteries to instruct it to direct that excess power onto the local loop down to its threshold (so it better be a smart 
meter that is connected to a solar panel system). When the microgrid controller finds that this is no longer needed, it 
will send a share_power_off command to that same meter to tell it to return to its normal mode of operation, sharing 
with the central utility as needed and available. 
# @427 Lossy algorithm options?
- Question: The spec tells us that the smart meter only has one choice of lossy algorithm, with averaging every 10 
readings. Is this the lossy algorithm we're stuck with, or are we free to implement other data collection and 
compression algorithms on board the smart meter?
- Tags: design_project
- Students' Answer: we can implement a better 
algorthim in the microgrid controller but not the smart meter. Smart Meter we cant change there programming
- 
Instructors' Answer: 
# @426 Base Level Bills
- Question: Do all customers (including apartments and emergency services) have a base level energy bill? Is it 
initially $20 for homeowners, $10 for each apartment unit, and $10 for each emergency facility? Who pays for the $10 
apartment/emergency facility solar panel farm meters (is it prorated?), or for the $100 broadband network?  And just to 
confirm, these base levels should be lowered if a property contributes more than it consumes one month, right?
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: 
# @425 Electricity Usage in Normal Operation
- Question: I'm a bit confused on how the normal operation use case works in terms of electricity generation/usage. It 
says that under normal operation there's enough sunlight to keep the batteries at 75% on average.&nbsp;  I assumed this 
meant that if there are $$n$$ houses in a microgrid, that the sum of all of their battery capacities divided by $$n$$ is
 75% (and one household has battery capacity less than 25%). However, as I considered more scenarios, such as 
transitioning from an outage, where all houses had batteries at say 10%, to the normal operation case, this would 
require that the battery capacity of all houses jump up considerably to average to 75% again.&nbsp;  What I'm most 
confused about is how this capacity is maintained based on electricity generation and electricity usage. We know that a 
full battery is able to allow up to 24 hours of average use, so say if the battery isn't charging, it goes down at an 
average rate of 100% / 24 hours. In order for the battery to be maintained at 75%, the average charging speed must also 
be 100% / 24 hours so that the average battery capacity is maintained at 75%. However, this wouldn't make sense in the 
transition scenario since the average battery capacity starts below 75%. It would require average battery generation to 
be much higher to bring the average capacity up to 75% before leveling out to 100% / 24 hours.&nbsp;  If this were the 
case, then we could theoretically generate infinite electricity by repeatedly sharing electricity from the residence 
microgrids to the power plant until it's full and still have an average of 75% battery capacity in the residence 
microgrids.&nbsp;  Can someone please clarify what is meant in the normal operation use case when it says that there's 
enough sunlight to keep the batteries at 75% on average? Thank you!
- Tags: design_project
- Students' Answer: 
- 
Instructors' Answer: 
# @424 Central Utility Controlling Electricity Distribution
- Question: Who would the central utility send a command to in order to for instance stop sending power to houses (so 
that it can be sent to emergency facilities)? Is it the power plant? Can we just assume that this can be done?
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: 
# @423 Question about microgrid controller data aggregation
- Question: Our team was wondering about the data that is required to be stored, which is power generation, power 
stored, and power through the meter. With the data format given, are we supposed to give all 3 data points in one event 
log every 15 seconds, or 3 event logs every 15 seconds?
- Tags: design_project
- Students' Answer: 
- Instructors' 
Answer: 
# @422 Storm Outage Residence
- Question: The DP Spec mentions that during a storm outage, a tree falls on one of the main power lines that serves 
half the residential microgrids, disconnecting them from the town power lines. Do we know which of the residential 
microgrids will be affected by this beforehand, or are they randomly disconnected?
- Tags: design_project
- Students' 
Answer: 
- Instructors' Answer: 
# @421 Broadband Network Capabilities
- Question: In the storm outage use case, it talks about a tree falling on the broadband company's lines to the central 
utility. What does this imply about the connectivity of the central utility during the storm? Is it completely 
disconnected from the microgrids so that they can't communicate or are they disconnected in another way?
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: 
# @420 Program the Smart Meter
- Question: How much can we program the smart meter. For example if we cant program them at all then if a communication 
failure in LTE happens then the smarter meter will attempt to do the previous command indefinitely until its best.  (Can
 we program better behavior without using variables or such?)&nbsp;  Or even a test where we PING the microgrid 
controller and isolate if no info gets throug?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: 
# @417 Smart meter recording
- Question: What does the data collected by the smart meter every 15 seconds look like? Does it contain both the history
 log and the event log? So is it 36+24 bytes or does it keep multiple records of history log for every record type?  So 
for example, in the apartment buildings, there's 1 smart meter for the solar panel. Does that one store `power 
generated` and `power stored` in two different history logs along with an event log? Is this the only smart meter that 
has a battery to store the power?  For the other 100 smart meters, are these ones only keeping `power in` data? So these
 ones don't have power storage?&nbsp;  Eventually, does the microgrid controller need the data from all 100 or does it 
only get from the solar panel's one to make decisions about sharing the power?
- Tags: design_project
- Students' 
Answer: 
- Instructors' Answer: 
# @416 Aggregation
- Question: I had a few questions about how aggregation works.  1) When the microgrid controller sends an instruction to
 aggregate from a smart meter, does it mean that from that point on, all the data collected by the smart meter will be 
sent to the microgrid controller until the microgrid controller instructs to deaggregate? 2) How does the smart meter 
send the data if it also needs to aggregate? Does it send every 15 seconds as it generates and then the microgrid 
controlled does the merging or averaging at its end? 3) When would we even need to use the lossless algorithm? 2GB is 
enough to send data every 15 seconds for a whole month and if there's an outage for some time and then the power is back
 since we have 10mbps speed of sending data, we can send the data that has accumulated relatively fast. So when would we
 need to use the lossless algorithm?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: 
# @415 Threads and processes
- Question: Spec asks for a design of "threads and processes" for controllers ("You will need to design the control 
structure (e.g., threads or processes) as well as storage management for the microgrid controller"). Our team is not 
entirely sure what we are expected to do here.  What is meant by control structure and how should we utilize threads and
 processes for that? Thank you!
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: 
# @414 Deficit round-robin
- Question: Assume that there is constant Zoom traffic but no email traffic for some time. It seems that with the 
algorithm described in lecture, the email queue would accumulate a lot of credit while the queue is empty. If this 
happens for long enough and email has a lot of credit, then it seems that email would be prioritized over Zoom traffic 
whenever an email arrives. Is there a mechanism that avoids it, e.g. not increase credit if queue is empty?
- Tags: 
lecture
- Students' Answer: 
- Instructors' Answer: This is a great question.  In practice, a queue only accumulates 
credit for rounds when it's non-empty. (You could easily augment the algorithm I showed in lecture by just putting the 
body of the loop inside an if statement -- if !queue.empty() or some such.)
# @413 DP - Solar Panel Relationship with 2 Smart Meters
- Question: We were confused on how the two smart meters in a given house interact -- specifically, should we assume 
that when energy is produced from the solar panel, it goes directly to the house and this is not recorded through the 
smart meters? That is, power produced that remains in the house does not get logged as an "outgoing measurement" on the 
solar panel smart meter and does also not get logged as an "incoming measurement" on the house smart meter (thus 
implying that the only incoming measurements are from the local line or central power plant / central utility battery 
and that the only outgoing measurements are to the local or town power lines)?
- Tags: design_project
- Students' 
Answer: 
- Instructors' Answer: 
# @410 DP Presentation Schedule?
- Question: I saw on the calendar that there's a week blocked out for DP presentations. Is there more information on 
scheduling? Are we presenting in tutorial, or at different slots throughout that week?
- Tags: design_project
- 
Students' Answer: 
- Instructors' Answer: You'll present to your recitation instructor outside of class. Your instructor
 will send out more scheduling information as we get closer to the presentation dates.
# @408 Clarification About Smart Meter History Log
- Question: What information does record_type and reading (in the history log) contain?
- Tags: design_project
- 
Students' Answer: 
- Instructors' Answer: 
# @407 Details About the 1-Min Auto-Transmit from Smart Meters
- Question: In the 1-minute auto transmission from the smart meters to microgrid controllers, what is sent? an entire 
record? Do we get to customize this at all?  It says homeowners have the option of setting a 1-minute auto transmit -- 
is this the same for the apartment buildings? How about police/fire/hospital?
- Tags: design_project
- Students' Answer:
 
- Instructors' Answer: 
# @406 Billing: Central Utility and Microgrid Controller Interaction
- Question: If the central utility is doing the billing, why does it need to regularly send billing rates to the 
microgrid controllers?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: 
# @405 Microgrid Controller RAM
- Question: The design project specs mentions that the microgrid controller has a "single processor machine," but it 
doesn't mention anything about the RAM. How much RAM does the microgrid controller have, and how much processing power 
does it have relative to the 256 GBs of RAM that the central utility has?
- Tags: design_project
- Students' Answer: 
- 
Instructors' Answer: 
# @403 DP Solar panels
- Question: I am a little confused about how the power sharing works: Suppose it is during the day and the sun is 
shining so all the solar panels are generating electricity and their batteries are charging. But for some reason, some 
batteries charge up to their threshold before others do. 1. Do we still want to instruct them to share their power with 
other homes even though the other homes just need time to charge up?&nbsp;  2. What happens to the electricity that we 
dump into the microgrid does it charge up the batteries faster or does it get wasted?
- Tags: design_project
- Students'
 Answer: 
- Instructors' Answer: 
# @402 What does this mean in the DPPR rubric?
- Question: Uses defined naming conventions to connect components/modules/messages of system.  Are we required to come 
up with special terms?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: We're asking you to use 
consistent terminology so that we can understand how concepts, components, or techniques appear in your system. If 
there's a standard technical term, use it consistently (unlike other genres where variety may be valued). If you do 
define your own name for a concept or task etc, use that same term consistently throughout.  This makes it possible for 
the reader to easily understand how those concepts, functions, etc appear and reappear in your system.
# @401 Command 'setup' not found
- Question: Using securecrt for athena. git clone only worked without ssh. ssh-ed into green-build. In /ethersim, setup 
ggo produced: &nbsp; &nbsp;Command 'setup' not found, but can be installed with: &nbsp; &nbsp; &nbsp; apt install ruby-
factory-girl-rails &nbsp; &nbsp; &nbsp; Please ask your administrator. Tried in and out of ssh. There was a comment 
somewhere that mentioned .bashrc, google produced that it may be: &nbsp; &nbsp;/etc/skel/.bashrc, this has a bunch of 
stuff but nothing stood out as interference. &nbsp; &nbsp;/home/hectormc/.bashrc DNE &nbsp; &nbsp;/root/bash.rc denied 
access unsure what else to try.
- Tags: handson3
- Students' Answer: Hi, try to add the following to the top of your 
.bashrc file: and then run That is what made it work for me
- Instructors' Answer: 
# @400 Hands-on 3 Q 4.2
- Question: Must we necessarily paste images to support our answer for whether the two routes are the same or is it ok 
to just say so?
- Tags: handson3
- Students' Answer: 
- Instructors' Answer: Include the relevant parts that support 
your answer
# @399 Destination of data on central utility
- Question: What should the central utility do with the data and billing information? In particular, should it send this
 information to some destination monthly? Should it keep this information around for a while (and for how long)?
- Tags:
 design_project
- Students' Answer: 
- Instructors' Answer: 
# @398 Canvas Gradebook
- Question: Despite our best efforts, there seems to be no way to show you only letter grades for assignments; Canvas 
forces us to have a letter-to-number mapping on the backend (see @295 for instance).  Please pay attention to our 
official grading policy on the course website, which explains the weights for each assignment, including some grading 
policies that Canvas can't capture at all (example: we drop your lowest hands-on score). Ignore the details of Canvas 
beyond your actual grades.  If you have any questions about your grade, we're always happy to clarify and talk to you 
about how you can improve (if you need/want to). Your TA is the first person to reach out to regarding grading 
questions.  
- Tags: logistics
- Students' Answer: 
- Instructors' Answer: 
# @396 Potential 6.033 in the News 👀
- Question: 
- Tags: other
- Students' Answer: 
- Instructors' Answer: 
# @395 DP Storm Outage
- Question: In the case of the storm outage, there is a period of time where the data network is down cuz the tree falls
 on the broadband company lines but the power lines are still up. Can the microgrids still get power from the central 
utility during this time or can we not because we can't make requests to the central utility?
- Tags: design_project
- 
Students' Answer: 
- Instructors' Answer: 
# @394 Units of W
- Question: In lecture, we talked about the TCP window being a number of packets, but in recitation my RI made it clear 
that TCP measures bytes instead of packets. This feels like a discrepancy to me. Which system is used in practice?
- 
Tags: recitation, lecture
- Students' Answer: 
- Instructors' Answer: In the real-world, TCP uses bytes.  For 
pedagogical purposes -- so in lecture and on exams -- we use packets. This is because talking about the window size in 
bytes leads to other complexities. Namely that sequence numbers and ACKs in the real world are also done with bytes (so 
there is a sequence number for each byte, not each packet). Getting into those details in lecture makes the more 
important points about the protocol much more difficult to understand.
# @393 2GB broadband limit
- Question: is this limit per smart meter / micro grid controller pair. For one micro grid controller and all smart 
meters in its control. Or for entire system.
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: 
# @392 DP FAQ
- Question: The FAQ responding to your questions posed in your Prep Assignments is located here: 
http://web.mit.edu/6.033/2022/wwwdocs/dp.shtml&nbsp;  It is now one of the many resources that can be found on the DP 
page on the website
- Tags: logistics, design_project
- Students' Answer: 
- Instructors' Answer: 
# @391 Fairness in Lecture 11
- Question: Assuming that network traffic is distributed equally among senders, it seems that senders could abuse the 
TCP protocol by creating several "sender nodes" that are used simultaneously and could use more network traffic than one
 sender could use. Is there any mechanism that avoids this, is the fairness protocol actually more sophisticated, or is 
it assumed that senders do not abuse the protocol like this?
- Tags: lecture
- Students' Answer: 
- Instructors' Answer:
 Great question! There is no mechanism built into TCP that avoids this.  However, there are plenty of scenarios where 
your outgoing link is the bottleneck. For instance, say you were at home, and the first network hop out of your home 
could carry ten packets per second. No matter how many TCP connections you generate from your machine, you won't be able
 to send more than ten packets per second.  Additionally, if you were trying to use multiple TCP connections to send a 
single logical stream of data to a destination, you'd have to do some complicated work at the destination to reorder 
packets. And if you don't have control over the destination, that might be impossible.
# @390 Battery threshold decision
- Question: Is the choice of 25%, 50%, or 75% for each residence made when the smart meters are first installed, or can 
homeowners change this value over time?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: 
# @389 What does this line mean from the rubric?
- Question: p. 3 http://web.mit.edu/6.033/www/assignments/dppr_rubric.pdf  "Each section builds its argument for 
systems' concepts and explains choices clearly, while acknowledging audience knowledge from the Design Project and 
discipline."
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: While you should explain, define, and 
justify your design and specific design choices, you don't need to re-explain things that your audience already knows 
very well. For instance, you don't need to fully re-state large amounts of material from the DP spec, and you don't need
 to define basic systems concepts like (these examples are not all relevant to the DP): modularity, or what BGP is, or 
why naming is important. 
# @388 Do we need to formally cite the DP Spec in our DPPR (or any other assignments going forward)?
- Question: Do we need to cite the DP Spec at all? Right now I just write (DP Spec, p. 5) or similar whenever I use a 
specific fact.
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: 
# @387 Homeowner Control
- Question: How much control does a homeowner have over their electricity? Can homeowners control when to share and who 
to share their excess energy with? For example, if there is no request for electricity within a residential microgrid, 
can a homeowner decide to share with the central utility or to keep and store it? If a homeowner has control of this, 
how do they notify the microgrid of this?  Or is letting homeowners have control over their power a design choice?
- 
Tags: design_project
- Students' Answer: 
- Instructors' Answer: 
# @386 Minimum Power Thresholds
- Question: On page 5 of the DP Spec, it says that "Each residence can set their threshold for the minimumamount of 
electricity below which they will not share. These can be set individually at 25%, 50% or 75%." This implies that each 
residence may have different minimums. How do the microcontrollers know the minimum threshold for each house?
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: 
# @384 FAQ for DP?
- Question: I remember hearing that there would be a FAQ sheet in response to our DP submissions? Is that out already, 
and if so, where to find it? If not, when can we expect it?
- Tags: design_project
- Students' Answer: 
- Instructors' 
Answer: http://web.mit.edu/6.033/2022/wwwdocs/dp.shtml  Under "Design Project FAQ"  (all of the DP-related content lives
 on that page)
# @383 "Isolate" command
- Question: As written, the Isolate command is irreversible. There is no "De-isolate" or equivalent command, and it's 
not even clear if rebooting will reverse it. Could such a command please be added to the spec?
- Tags: design_project
- 
Students' Answer: 
- Instructors' Answer: 
# @381 In fast retransmit / fast recovery, is 4 an arbitrary constant, or is it W - 1 in general?
- Question: Mostly just the title. I'm confused if this varies based on window size, and why not, if it is an arbitrary 
constant.
- Tags: lecture
- Students' Answer: 
- Instructors' Answer: It is not W-1 in general (thanks for asking that; 
that's not clear from the slides!). 4 is the typical constant (original ACK + 3 duplicate ACKs). I wouldn't say it's 
arbitrary. It's a tunable parameter for TCP, but 4 works well in the majority of networks.
# @380 What power does smart meters measure
- Question: For the smart meters on houses, do they measure power sent and used within the microgrid? If not, how do we 
keep track of which house is using power for data collection?
- Tags: design_project
- Students' Answer: 
- Instructors'
 Answer: 
# @379 Hands-on Q5 - can't clone directory
- Question: I was able to ssh into green-building-tetris but when I run git clone 
https://github.com/jaytlang/ethersim.gitI get the error "fatal: could not create work tree dir 'ethersim': Permission 
denied " and I'm not sure how to fix this
- Tags: handson3
- Students' Answer: 
- Instructors' Answer: Update: When 
using athena locker (ie. not your local terminal), get the ethersim folder (via git clone if possible) before ssh-ing 
into green-building-tetris. If git clone still doesn’t work, run the following commands: wget 
https://github.com/jaytlang/ethersim/archive/refs/heads/master.zip unzip master.zip mv ethersim-master ethersim
# @378 Central Utility Prediction
- Question: hi my team was thinking of adding a simple prediction model to the central utility to determine when and how
 much electricity it should buy from the regional grid if it needs to.  I did see on the dp though that it says that we 
don't need to handle model or prediction for demands that the MIT researchers want to do but provide the data to do so 
(sec 1). However, it also says the town needs to 'predict its overall costs to set monthly rates ahead of time and to 
plan how best to manage its resources. Your control system will enable this functionality" (sec 2.1). I  So, overall, is
 this saying that we can/should add a way for the system to be able to predict its costs and how to minimize costs to 
residents?&nbsp;
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: 
# @376 Write up recitation answers on paper?
- Question: I noticed this week's readings have different directions. Should we assume that we shouldn't expect the 
normal turn-in method (e.g. Google Form) this week?
- Tags: recitation
- Students' Answer: 
- Instructors' Answer: Nope!
 Sorry! You should instead expect that I made a mistake on that page on the website, and will update it in just a moment
 :).
# @375 Links for Lectures 11 and 12
- Question: Lecture 11: https://mit.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=ce9ced0e-c2fd-4a91-a93e-ae4f00d6afed
 Lecture 12: https://mit.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=97ff9ec3-8a39-4209-b041-ae4f00d6f38a  Slides 
will be on the website before each lecture so you can follow along.
- Tags: lecture
- Students' Answer: 
- Instructors' 
Answer: 
# @373 Hands-on 3, Q5.1
- Question: I'm confused how the structure of the ethernet differs from the paper. They both have only one path between 
all pairs of nodes, and they're both unrooted trees from the diagram. I don't understand what the paper means by saying 
their structure is the dual of a star network?
- Tags: handson3
- Students' Answer: 
- Instructors' Answer: Ethersim’s 
star topology means that all traffic goes through the “central routing node”. What might this change in our protocol? 
The paper says that ethernet is a “dual” of a star network, likely meaning as inverses of each other. They say that 
Ethernet has central interconnection but distributed control, while a Star Network has distributed interconnection, but 
central control.
# @372 Handson 3, Q3.1
- Question: I found that traceroute (from Athena) failed to find my laptop (online, using MIT secure wifi). Is this 
normal?
- Tags: handson3
- Students' Answer: 
- Instructors' Answer: Yes this can happen! Why do you think it may have 
failed?
# @370 Packets central utility <> controller
- Question: What is the max size of the packet that we can send between central utility and controller?  In addition, 
since we can design the communication between the central utility and controller, can we design our commands in addition
 to the ones mentioned on page 6?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: 
# @366 Reduce demand
- Question: When the central utility asks a microgrid controller to "reduce demand," what does a microgrid controller 
need to do to make this happen? Is it responsible for physically stopping more power to flow into the local power line 
or it needs to communicate this info to smart meters to make this happen?&nbsp;
- Tags: design_project
- Students' 
Answer: 
- Instructors' Answer: 
# @365 Hands-on 3 Q4
- Question: "If the Stanford traceroute does not work, or if you get no reply after 2-3 minutes, you should try one of 
the other looking glass servers."  What qualifies as not working in this context? I wasn't sure whether we expect this 
to succeed since the next question ("Which of the traceroutes succeeded or failed?") implies that it's normal for 
one/some of these commands to fail.
- Tags: handson3
- Students' Answer: 
- Instructors' Answer: I think you only need 
to resort to this if neither of them works (trying not to give away which should and should not work!)
# @364 Smart meters configured to send data automatically
- Question: For the smart meters that are configured to send data every minute, do they send all the data in their 
databases or the microgrid controllers can specify with "Initialize" what to be sent and also change later the kind of 
data being transmitted (potentially through "get")?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: 
# @363 lossless vs. non-aggregated data
- Question: Is there ever a scenario in which we would prefer to not aggregate our data vs. doing lossless data 
aggregation? The spec mentions nothing about any power or time requirements to perform lossless aggregation, and it 
seems that lossless data aggregation would always be better.
- Tags: design_project
- Students' Answer: Lossy algorithm 
compress the data a lot more. We are limited to sending 2GB a month of data over the network and if communication is 
down we may want to compress data further to send larger packets.
- Instructors' Answer: In the lossless aggregation 
mode, the meter communicates its state less frequently. If your design uses this communication to determine if the meter
 is working, the lossless mode will increase the time it takes to detect failures. See comment on @363_f3.
# @362 Excess Power to Central Utility
- Question: How is electricity shared with the central utility? Do sites who want to share their excess do so 
automatically or are they instructed by the microgrid? Can the microgrid controller stop a site from sharing their 
excess with the town so that it stays within the microgrid?
- Tags: design_project
- Students' Answer: 
- Instructors' 
Answer: 
# @361 Are power and data networks delineated?
- Question: My team's current understanding is that the battery life of the microgrid controllers and smart meters is 
there for use in the case of power outages or similar - how do these components' batteries get recharged after 
depletion? If they are connected to the power being sent through them, what kind of draw does this put on the shared 
power?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: 
# @360 Solar farm battery capacity
- Question: The solar farm servicing the emergency services is specified to have a battery minimum of 75% and is the 
locus of power sharing between the hospital/police/fire - but what is its battery capacity?
- Tags: design_project
- 
Students' Answer: 
- Instructors' Answer: 
# @359 Why do the apartments only have 1 smart meter?
- Question: If the apartments can share power with the central utility (pg 5), then doesn't there need to be 2 smart 
meters? One for tracking the amount of incoming electricity and one for tracking the outgoing electricity?
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: Resolved in follow-up.
# @357 DP Prep Technical Feedback
- Question: When/where can we see technical feedback for the dp prep assignment? Trying to apply that feedback for the 
preliminary report.
- Tags: design_project
- Students' Answer:  http://mit.edu/6.033/www/assignments/dp_faq.pdf  
Technical feedback refers to this FAQ, and we should get more individual feedback this upcoming Friday based on the 
calendar.
- Instructors' Answer: 
# @356 Having trouble with ssh green building
- Question: I think this happened after I tried opening multiple command windows logging into ssh for section 6. I get 
the response ssh: connect to host mit.edu port 22: Operation timed out and I suspect it might have been to too many 
requests at once since I’ve had similar errors before where that was the cause. However, that was several hours ago and 
I’m still unable to log in and cannot complete section 6 of my handson because of this. How do we resolve this issue?
- 
Tags: handson3
- Students' Answer: Resolved: for anyone else with the same error, make sure you’re doing .mit.edu and 
not @mit.edu
- Instructors' Answer: 
# @355 Battery confusion
- Question: I just realized that there is confusion about batteries. There were some very good questions primarily 
privately but now on piazza as well. Each solar panel system has a battery bank that provides significant backup power 
storage.Separately, I added because several people pointed out to me that it was missing, that each microgrid controller
 and smart meter has its own little battery, in case the power goes out, so it can keep working. These are batteries of 
the sort you find in your cell phone. They are integrated into the devices and only serve to allow the devices to 
continue to operate. They will not heat houses or run the AC. They are only designed to allow the devices that comprise 
your system to continue operating under dire circumstances. You cannot do anything with them other than assume that for 
all intents and purposes the microgrid controllers and smart meters will never go down.
- Tags: design_project
- 
Students' Answer: 
- Instructors' Answer: 
# @353 **Get** request on specific log fields
- Question: Can the microgrid controllers send Get requests only for a subset of the fields in the smart meter 
history/event logs?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: Yes. It can specify both which 
types of data it wants and how many records.
# @352 Maximum power supplied by batteries to the grid?
- Question: Is there any limit to the rate at which batteries (e.g., attached to houses) can supply power to the micro 
or central grids? Suppose all batteries in a microgrid are full and so their smartmeters are instructed to share power 
with the central grid. It seems like there is nothing preventing all of the energy in the batteries being consumed by 
the central grid over a very short window of time. In particular, if this happens in less than 15s, there seems to be no
 way for the microgrid controller to prevent this undesirable outcome.
- Tags: design_project
- Students' Answer: 
- 
Instructors' Answer: I'm not an electrical engineer, but there certainly are limits on how much power can be transmitted
 through a wire without it blowing up or burning up. The electrical system will control that. I suspect (and let's 
assume for purposes of this project) that the rate at which electricity can be generated by all the solar panels in each
 microgrid is below the level that will overload the wires.
# @351 Commands To Smart Meters (Size, Place?)
- Question: Do commands (simplified version of the ANSI C12 protocol) to smart meters travel through the broadband 
network? (i.e. do they count towards our 2GB limit?)  If so, how large is each command?  Thanks!
- Tags: design_project

- Students' Answer: 
- Instructors' Answer: You can assume that a command fits into a single packet. Their impact on the
 network will be so far below negligible that you don't need to worry about them.
# @350 Local Loop Resource + Microgrid Power on Loop?
- Question: In @245, it was mentioned that there is a "local loop within the microgrid."  Is this literally a loop, i.e.
 there are are wires forming a loop between all the houses? In this case, does that mean this loop cannot "store" energy
 to save for later?  Or, does the microgrid also have access to some battery which holds power for the entire local 
area, for houses to freely draw from or add to?  In either case, the microgrid is stated to have its own battery to 
support its own operation. How can it refill its own battery?  Additionally, what does it mean for a microgrid to have 
smart meter functionality?&nbsp;
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: Actually, a 
microgrid controller does not have a battery. There is no microgrid wide battery in the normal system. Except for the 
CMLC, all batteries are only associated with solar panel systems.   About microgrid controllers and smart meter 
functionality. The microgrid controllers are the consolidators of the information collected by the smart meters, so from
 the perspective of the central utility, the microgrid controllers provide the information from the houses, apartments, 
buildings and solar panel farms to the central utility.
# @348 Suggested report format?
- Question: In the tutorial videos for next week, the WRAP instructor recommends having the following 
sectionsIntroduction System Overview System Design Conclusion  but on the DPPR rubric, it says that the report should 
have these sections  Problem Statement System Overview System Description Use CasesSummary  Which one should we follow?

- Tags: design_project
- Students' Answer: 
- Instructors' Answer: Great question.

Mostly this is a result of the 
rubric calling out explicit subsections. While this will be discussed in more depth next Friday, The Introduction will 
include a problem statement as well as a high level discussion of the solution. You can see examples of how this works 
in both the exemplar papers and the research paper introductions read for class. Here, the introductions describe a 
problem space and then explain how they will address that problem space. These two moves are the fundamental goals of 
the introduction.

In a similar way, the system design includes the system description and use cases. Summary and 
conclusion are synonyms and we'll fix that misalignment in the future.

So think of the structure as:  Introduction 
(Problem Statement, Intervention Statement) System Overview (High Level Overview, System Diagram) System Design (System 
Description, Use Case Analysis)
Summary/Conclusion
# @347 Solar Farm Batteries
- Question: I know that the solar farm has batteries (in essential service microgrid) but does it store power or does it
 share at 0% (since it should not be consuming more electirty then it produces).  Or should we just treat it like 
another building 
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: There are three "types" of 
microgrids in this story. The most general one is the microgrid of houses in which each house as a solar panel system 
and batteries. I think sharing there is pretty clear. The next is the apartment buildings. Again, I think sharing is 
pretty clear there. If one building's batteries drop too low the others, if they have excess, will share. The third is 
the municipal buildings. In this case, the sharing is that they all use the single solar panel farm and its batteries. 
There is no other microgrid sharing possible. Instead, if those batteries are full, the only option for reducing cost is
 to send the excess power back to the CMLC through the outgoing smart meter and get credit for it.  That all said, for 
the municipal building microgrid, if the solar panel system has no more power to give to the buildings (its battery 
system is essentially at 0%) each building will automatically be serviced by the town system and that will go through 
their meters. They will be charged for their usage.
# @346 Technic feedback
- Question: Who should we go for technical feedback of DPPR? Is it our recitation director?
- Tags: design_project
- 
Students' Answer: 
- Instructors' Answer: You'll receive written technical feedback from your recitation instructor on 
the DPPR, though not a technical grade. If you want some technical feedback in advance, your recitation instructor and 
TA are great resources for the feedback.
# @345 Clarification on what a design property is?
- Question: In the rubric, it states that a developing paper has "Lists too many design properties (3 or more) instead 
of focusing on the system's main priorities; or doesn't identify any properties as focus." What exactly would count as a
 design property? Thank you!
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: Design properties, 
sometimes called design principles, are the value statements that describe the system goal(s) of a design as opposed to 
specific behavior or application goals in the use case. Design properties or principles include simplicity, scalability,
 fault tolerance, security, correctness, etc.
# @344 How to add things like reliable transport?
- Question: I read the spec to read that we need reliable transport for the data entries. I was wondering how/if we add 
this on top of things like LTE?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: Your phone supports 
TCP on top of LTE. It is definitely an option for you to use.
# @343 Confused about network?
- Question: We cannot pick the routing protocol for either broadband or LTE (or really any of the networking in this), 
correct? Our devices are just connected to some pre-existing network of machines that provide connection through some 
pre-determined routing protocol?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: Yes. Let me say it 
differently. You do not need to pick (or design) the routing protocol used by the network layer. The network layer is IP
 and routing is whatever is used in and among the various ASs in play.
# @342 How is billing Calculated?
- Question: If the central utility bough electricity during the non-peak hour and stores it, then residents use these 
during peak hours. How should they be billed? By the lower rate or the higher rate or some average rate?
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: I believe the answer is buried in the spec. Power that is 
credited to customers' bills is always credited at the off-peak rate. Power used is charged based on the time of day.  I
 know this may seem a little unfair, but in the town I was using as my example, this is actually how they do it.
# @341 Excess power in central utility
- Question: Sorry if this was asked before, I couldn't find something similar:  Can the central utility buy power 
without immediate demand? If so, what happens to the purchased power that isn't used and can't be stored in an already-
full battery supply (if it's thrown away, can central know how much is being thrown away)?
- Tags: design_project
- 
Students' Answer: 
- Instructors' Answer: It actually wasn't not asked before, although I just mentioned in the very 
previous question. Yes, it can buy power whenever it wants and it can decide whether that power should go into the 
batteries or be used to service customers directly. You will want to think about this in your design.
# @340 Routing Electricity to Smart Meters
- Question: If a property is running out of power (say &lt;10%) and there is no other property within the microgrid to 
share with it, does the microgrid controller automatically start sharing its own 48-hour battery capacity with that 
property, or do we need to start and stop this process?  Also, if the controller does not have enough battery power 
either, do we send a command to the central utility saying to route power? Do we specify which property the power should
 be sent to? And then do we tell the central utility to stop sending power when the property has enough?  
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: I think you're slightly confused. The only batteries are at 
the solar panel systems and in the central utility. There are no batteries "owned" by the microgrid controller. If the 
microgrid controller discovers that a house's batteries are very low, and if it knows that some of the other houses in 
the microgrid are above their thresholds, it will command one or more of them to provide power to the microgrid. If that
 doesn't happen, when the house gets down to a point where the battery system won't give out power (probably not quite 
zero, to preserve the batteries themselves), the house system will automatically switch to the CMLC power and begin 
receiving from the town (and being charged for that).  Separately, the CMLC has two sources of power from which to 
service the town customers, its own batteries and the regional utility. You may want to think about exactly what happens
 in terms of its balance between using regional power to service its customers vs. keeping its own batteries topped up.
# @339 Possible Failures
- Question: Is it possible for the smart meters or microgrid controllers themselves (or central utility) to fail and 
ignore commands, or is it only the power and data networks between them that can go down?
- Tags: design_project
- 
Students' Answer: 
- Instructors' Answer: In real life, absolutely. But we're not considering that at this stage. We are
 assuming they are 100% reliable.
# @338 Smart Meter Reading
- Question: In a history log entry, does the 64-bit reading contain the "Power generation", "Power stored", and "Power 
through the meter"? Or are there 3 copies of history log entry sent every 15 seconds?
- Tags: design_project
- Students'
 Answer: 
- Instructors' Answer: No, That is what the record type is about. We have 3 types of records here. If they 
were all clumped into a single record, aggregation would likely be almost impossible to achieve.
# @337 Drawing the diagram
- Question: Is there any suggested tools that we can use to draw our diagram in the DPPR?
- Tags: design_project
- 
Students' Answer: 
- Instructors' Answer: Let me remind you that your system is not the system depicted in the figures 
in the spec. Those figures are depicting the underlying system, on top of which you will be designing your system.
# @336 Can the smart meters communicate directly with the central utility?
- Question: I don't really understand why they couldn't, but the diagram on page 4 of the DP Spec doesn't really seem to
 show this as a possible connection.
- Tags: design_project
- Students' Answer: According to @285 I don't think so :(
- 
Instructors' Answer: 
# @335 Priority for power
- Question: The FAQ addresses what happens in the case that microgrid power isn't enough to meet demand and mentions 
that the system doesn't set priorities. The FAQ does not address a question I had in my DP Prep assignment about how the
 priorities are set in the case of an outage or reduced availability of power from the external grid (as mentioned in 
section 2.2.3). When this occurs, how much priority should be given to emergency services and the subsidized apartments 
before power is distributed to the houses? Should the system fulfill all of the needs of the emergency services first, 
then the apartments, and finally the houses, or is there a different intended distribution of energy?
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: The design of the electrical system is that every building 
has a service level (the ampere service) for which it has contracted. The CMLC agrees that it will provide that much if 
the solar systems cannot. Furthermore, the agreement that the town has the the regional utility is that it will provide 
that much, if needed. So, the problem arises if the regional utility cannot live up to its agreement for some reason. 
One reason is that everyone designs for average not peak behaviors. We saw that in Texas a few years ago. So, there may 
be times when the regional utility cannot provide enough. Even worse, we have certainly seen large scale or localized 
power outages, when the regional utility may not be able to provide any power.  So the rest of your question is a good 
question. Thinking about priorities may play a role in your design, for sure. You may want to think about various kinds 
of stakeholders to consider this question.
# @334 Microgrid Controller Smart Meter Functionality
- Question: The MicroGrid Controllers are said to have smart meter functionality. Does this mean that there is a smart 
meter measuring the inflow/outflow of electricity to the microgrid and sending data to the controller?
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: They are "smart" in that they are not the old traditional 
meters that simply collected an aggregate of how power had gone through them and a person would come around (and later 
drive by with a radio) to read the current reading once a month. These meters, as you can see collect and keep track of 
a number of things happen every 15 seconds and keep track of them. They also can handle the business of sharing power on
 the microgrid. And, yes, they send this all either under their own control or on demand. (See the updated version of 
the spec for this.)
# @332 Monthly rates calculations
- Question: How far in advance are monthly rates calculated, i.e. for March, when do we find out how much we are going 
to pay for one purchased unit of power?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: If this 
matters to your design, you should specify it and explain why it matters.
# @331 Network layers
- Question: In the DP spec, we were given information about 2/4 layers for communication between controllers and smart 
meters (ANSI - application layer, LTE - physical layer)? In our design, do we need to worry about the protocols that are
 going to be used in the routing and forwarding layers ?
- Tags: design_project
- Students' Answer: 
- Instructors' 
Answer: No, you do not need to design the network layer. Every device in the system has an IP address. You might want to
 think about whether using TCP or UDP would be more appropriate. We will be talking about TCP over the next week, so 
this may be a bit of the design that you might leave open for now.
# @329 Billing in central utility
- Question: Do we need to design the billing system that central utility will be using or do we just need to make sure 
that we provide enough information for that system to work (i.e. monthly energy use/generation for each building) ?
- 
Tags: design_project
- Students' Answer: 
- Instructors' Answer: You need to provide enough information for the CMLC to 
do its billing, but you absolutely do not need to design the billing system.
# @328 DP - Billing
- Question:  Is each apartment household billed separately? In other words, how do we keep track of each apartment 
room’s electricity consumption if we only have two smart meters?  Does billing have to be done at a building-specific 
level? Or can we bill the entire microgrid and separate them into each individual house/apartment?  Are the police, 
fire, and hospital billed separately?  
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: I'm not sure 
I understand. Every customer gets their own bill. That is each apartment, each house and each municipal building. This 
is untreated to which micrograms they belong to.
# @327 DP Follow-up question about in-grid sharing
- Question: To follow up on https://piazza.com/class/kyypdylj1dk646?cid=220_f1:Can we confirm that power shared within 
the microgrid does not go through any smart meter? And if this is the case, how would it be possible to keep track of it
 for data collection purposes, as is desired (page 6)?
- Tags: design_project
- Students' Answer: 
- Instructors' 
Answer: I've added an additional answer in @220. Please see that and let me know if you still have a question.
# @326 Purchasing power by central utility
- Question: What is the delay from central utility sending the request to purchase power to the delivery to its storage?

- Tags: design_project
- Students' Answer: 
- Instructors' Answer: There is no delay. Part of what the electric system 
does is to make sure that from whatever sources there is continuity of delivery (unless there is a power failure).
# @325 Network used in communication central utility <> controllers
- Question: DP spec mentions that  "The central utility is on the local broadband service. Notice that the LTE and 
broadband services interconnect." (p. 4). I'm not sure if I fully understand how it works. Does it mean central utility 
communicates with controllers using LTE? If so, what is the purpose of broadband service then? How is it possible that 
LTE and broadband services interconnect?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: See @214. 
The LTE and broadband networks are interconnected in the same way as your phone and MIT's web servers are. You do not 
need to worry about this. The discussions about layering in lecture and recitation should help you to understand this 
better.
# @324 Electricity sharing policy
- Question: Can a building share electricity out of its microgrid if every other battery in the electric system is 
full?Is a building forced to share electricity if its battery is over the set threshold, or can the microgrid controller
 choose to not command it to share electricity? 
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: I 
don't quite understand your first question. Notice that one of the kinds of information collected is the battery level 
of every set of batteries. The microgrid controller should be receiving this from any of its smart meters. If the 
microgrid is one of houses, it will know when a house is getting very low and will also know whether others in the 
microgrid have more than their settings. For any of those, it can request that each of those share their excess. If none
 of the houses has excess, the home's only choice will be to depend on the town utility for power (for which it must 
pay).   If the situation is one of the solar panel farms (apartment buildings and town buildings), the only choice is to
 use the town utility and pay for it.  To answer your second question, yes, a house is required to share any excess 
above its threshold, if requested. If it is not requested (all the others are over their thresholds) it is not required 
to share.
# @323 Protocol between Central utility and controller
- Question: DP spec mentions in smart meter section (p.6) "the protocol available to you is a simplified version of the 
ANSI C12 protocol". Is the same protocol used in the communication between central utility and controllers, or is it 
only between controller and connected smart meters? Page 11 also adds that one of the tasks is "designing the commands 
exchanged between the central utility and the microgrid controllers" so I'm not 100% sure what the constraints are for 
the communication between the central utility and the controllers
- Tags: design_project
- Students' Answer: 
- 
Instructors' Answer: The protocol elements you mention are those specified for communication between the microgrid 
controllers and the smart meters. Defining the equivalent of what happens between the microgrid controllers and the 
central utility is part of your challenge.
# @322 Smart Meter Reading Granularity
- Question: What units are the smart meter readings in (i.e. how fine-grained are they, as this would play a role in how
 effective lossless aggregation is)?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: 
# @320 Etiquette in posting questions about the DP on piazza
- Question: If you have more than one question about the DP, please create separate posts for each topic. A topic may 
have more than one question, but if your questions are on multiple topics, please use the summary field to identify the 
topic, so your classmates know where to look for answers.
- Tags: design_project
- Students' Answer: 
- Instructors' 
Answer: 
# @319 OH
- Question: Is there OH today?
- Tags: handson3
- Students' Answer: 
- Instructors' Answer: Yes!  Feel free to join the 
queue :)  https://queue.mit.edu/6.033/queue
# @318 March 11 Tutorial Vids?
- Question: Will there be videos assigned for March 11's tutorial? If so, is there an estimate for when they'll be 
posted? Thanks!
- Tags: tutorial
- Students' Answer: 
- Instructors' Answer: We typically post the tutorial videos a 
week or so ahead of time, so they should be up by tomorrow.
# @317 Cannot run 'setup ggo'
- Question: Title - it says 'setup' is not found
- Tags: handson3
- Students' Answer: 
- Instructors' Answer: Did you 
have any luck resolving this issue? Perhaps the discussion in @379 may be useful
# @316 Hands On 3 Q2
- Question: Is this question asking us how the initial path is found, or how traceroute determines what that path is? If
 it's the latter, is it okay to just summarize the process described in the man page?
- Tags: handson3
- Students' 
Answer: 
- Instructors' Answer: I would say the latter, and yes, try to explain what's going on as you understand it.
# @314 What are the network guarantees provided by the LTE connections?
- Question: In addition, is the connection between microgrid controllers and central utility also LTE-based? If not what
 are the guarantees for that as well?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: I'm not sure 
what you are looking for in terms of guarantees. There are few absolutes in this world. LTE generally provides lower 
throughput and higher latency than broadband. It is support IP, so the delivery of packets at the netowkinrg layer is 
best effort with no guarantees. TCP or other transport protocols will do their best to provide improved semantics and 
behaviors at perhaps higher cost.  Separately, just as with your phone sitting on an LTE network, you can access 
webpages and other services on websites, etc. which are not on the LTE network. The LTE network internally has a set of 
connections into the wired network. So, the microgrid controllers only use LTE and the central utility only uses 
broadband, but as we've discussed in our layering discussions this week, traffic can flow across those link layer 
technologies with a network layer (IP) and probably a transport and application layer protocol spanning across those 
translations at the link layer.
# @313 The message-passing paradigm of dialup internet
- Question: It seems that dialup internet was an overlay onto the existing widespread telephone line network, which was 
a circuit switched system, correct? Was internet communication still operating on a packet-switched protocol then?
- 
Tags: other
- Students' Answer: 
- Instructors' Answer: Yes, the internet was still packet switched. Those packets were 
being sent over the phone lines, between end-users and their ISPs. The phone lines were circuit switched, but that was 
an implementation detail.
# @312 Using a server other than Athena
- Question: What are the other servers that we could use if a traceroute to Stanford's server does not work on 
Athena?&nbsp;
- Tags: handson3
- Students' Answer: 
- Instructors' Answer: Stick with Athena, but if Stanford isn't 
working, you could use any of the other looking glass servers (http://www.traceroute.org/#Looking%20Glass).
# @311 Hands On 3 Release?
- Question: When will the networking hands-on be released?
- Tags: handson3
- Students' Answer: 
- Instructors' Answer: 
In exactly 29 minutes (12 PM) (not me trying to post this at exactly 11:31 AM)
# @310 Paths question in 5.1-5.2
- Question: Hello,  I am currently trying to answer question 5.1-5.2, and am a bit stuck. I know that cd'ing into ~ 
gives you (/afs/athena.mit.edu/user/), which is different from (/mit/YOUR_USERNAME), and i think /mit/YOUR_USERNAME is 
only a symbolic link.  I think when we do cd ../YOUR_USERNAME from directory /mit/6.033, this is simply interpreted as 
going back one dir and then going to YOUR_USERNAME. But am not sure how one would fix these commands to get from 
/mit/6.033 to the actual address at ~.  Any input would be greatly appreciated!&nbsp;&nbsp;
- Tags: handson2
- Students'
 Answer: For 5.1, I found it helpful to cd to /mit and print the contents of that folder with ls. You might also want to
 try a pwd after cd /mit/6.033 to see where that takes you! For 5.2, I found this answer helpful: @178
- Instructors' 
Answer: 
# @307 DNS and the networking stack
- Question: Does a DNS request/response process happen through the same networking (internet?) stack we've been 
discussing? Which part, if any, could be classified as part of the application layer of that process?
- Tags: other, 
recitation, lecture
- Students' Answer: 
- Instructors' Answer: DNS itself is an application layer protocol. So a 
message from a DNS client to a server would be an application-layer message, which would get encapsulated by layers 
below.
# @306 Microgrid instructing smart meters to share power
- Question: The DP spec says [page 5, third to last line] that "Within a microgrid that contains more than one set of 
batteries, if any of them is below its minimum and others are not, the microgrid controller will instruct the others 
above their minimum to share, so that all are brought to their minimum".Does this mean that the microgrids have the 
capability to communicate and control how much the smart meter connected to the in-going power will draw, and how much 
the out-going power will share? If so, which part of the communication protocol between microgrid and smart meter is 
responsible for this?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: See @225. There are two 
operations that the spec writers forgot to include. They will come as a correction in the next day or so, but in the 
meantime you can assume that they will be there.
# @303 Charging batteries
- Question: 1. Can power delivered from town charge residents' batteries? ie can residents buy electricity throughout 
the night to charge their batteries to lower costs during the day?&nbsp;  2. Can a homeowner decide when to use their 
batteries or this is only handled through the microgrid controllers? 
- Tags: design_project
- Students' Answer: 
- 
Instructors' Answer: 1. yes, power from the town can be used to charge batteries, and it is a really good idea to do 
this, if needed, during non-peak hours. This will also be true of the batteries managed by the central utility - they 
are least expensively recharged in non-peak hours.  2. The absolutely optimal thing for a homeowner to do is to use 
their private battery supply first. The other members of their microgrid, the other source of non-charged power, does 
not come with a guarantee. It may simply not be available. The third source of power is power lines from the CMLC. That 
will always have some cost associated with it.
# @302 Hourglass protocol
- Question: What does it mean that IP is an hourglass protocol? This term was used many times in recitation today, but I
 don’t know what it means.
- Tags: recitation
- Students' Answer: 
- Instructors' Answer: We often talk about an 
hourglass model with IP as the "narrow waist" of that hourglass. Here's a diagram (this one is from 
https://en.m.wikipedia.org/wiki/File:Internet-hourglass.svg, but google "IP hourglass" or similar and you'll see lots of
 similar images):     This is illustrating protocols that live at different layers -- application-layer protocols such 
as Email, VoIP; transport-layer protocols such as TCP, UDP; network-layer protocols such as IP; and then link-layer 
protocols beneath that. This particular diagram has split the link layer into two separate layers (sometimes we use the 
term "physical layer" for the bottommost layer and "datalink layer" for the layer above that).

Notice that at the 
network layer, we have a single protocol: IP. For every node on the Internet to talk to every other node, at some level,
 there has to be a common protocol.
# @301 Programmable
- Question: What is the meaning of programmable? does that mean that my design can heavily depend on function\ tables I 
am created in the Microgrid controller + central utility or is it just for suggestions for new capabilities for the next
 iterations?
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: The first. You have freedom to decide 
what data structures, stored data, and operations are required for the central utility and microgrid controllers to do 
their tasks. You should consider them to be programmable devices, in contrast with the smart meters which are black 
boxes that respond to a limited set of commands and will send data in only the specified formats.
# @300 DP - Smart Meters
- Question: 1. What does the Initialize command do to a smart meter? does it reset all measurements to zero?  How long 
does a reboot take? In that time power used during the time of reboot will or will not be counted for?   Are the smart 
meters passive or active devices? can a smart meter send data actively to a microgrid controller? If so, does that mean 
they are programmable? In 2.2.2 point 1 it says smart meter can issue put command to a microgrid controller, but if the 
smart meters are not programmable, how will we initiate such put?   History table has start time and end time for each 
value. Is the reading value saved is the delta = reading at end time - reading at start time, or is it just the reading 
at end time?   Houses that have two smart meters - one of the smart meters measures incoming electricity, the other 
measures outgoing.a. Which one is connected to the battery?b. If we send a command, do we need to send it to both 
meters?c. Can we assume all data, except power through the meter is equal for both smart meters?   What exactly the 
isolate command does? Is it disconnecting a house from local microgrid + town electricity so the house only runs on its 
batteries? or does it mean the house will just be disconnected from the town electricity but will still be sharing\ 
receiving electricity from in-microgrid?   Aggregation - does it apply to all data stored? According to the command 
dictionary:Deaggregate: this returns the smart meter to no aggregation of transmitted data.So aggregation only applies 
to transmitted data but not stored data? If so, does the smart meter find the requested data, copy it, does the 
aggregation, and then sends the data without any changes to the actual data stored?   State changes - it seems there are
 two sets of states, but the event log accounts for them all as one. If I have the following state changes:(1) 
aggregating data(2) running disconnected(3) running on the power netDoes this mean that while it ran disconnected, it 
didn’t aggregate data anymore? or did it continue aggregating data until it received another command?   What are the 
commands for sharing electricity? If I want a smart meter to start sharing with a local microgrid? or if I want to start
 selling. The spec says the latter happens immediately, but what happens when the batteries for the CU are full? Where 
does the power go?   The diagram in the spec shows the central utility is connected through a network connection and the
 actual power lines are through the regional utility. How does the power share of the central utility battery happen 
then?   @245 states that there are two sets of wires going to each house; one for the local in-microgrid share, the 
other for the electricity from\to the town where the meters are connected to. In the spec it states that we will have to
 find a way to not account for electricity share within a microgrid, but if the meters don’t count that, then, wouldn’t 
the calculation for power bought\ sold just be what the meters read for power passed through meter?    
- Tags: 
design_project
- Students' Answer: 
- Instructors' Answer: In general, it would great to ask questions on a single topic
 in each piazza post, so everyone can find the questions and answers by topic. But for the moment, I'll dive into these 
11 questions.  1. What does the initialize command do? It (re)boots the device. That will not erase anything stored on 
the persistent storage. Data will be deleted from the local persistent storage once there is confirmation that it has 
reached some other persistent storage. So, for a smart meter, once a record is confirmed to have reached its microgrid 
controller and is stored there, it will be deleted from the smart meter's storage. Any records not deleted before a 
smart meter shuts down (for whatever reason) will still be there to be available to be sent after an initialization.  2.
 Rebooting is relative fast, under 10 secs. You do not need to worry about power utilization not accounted for during 
that time.  3. Are smart meters passive or active: Here is another minor update to the spec. When initialization of a 
smart meter occurs, the default is to set the smart meter to push its data once a minute. But, under homeowner control 
the meter can be set to not send data at all. This will be a hardwired switch on the meter itself. The response to the 
initialization command will be to send an acknowledgment that reports whether smart meter sending of data is on or off. 
This way the homeowner has control of this and the microgrid controller knows that it may need to request data from the 
smart meter on a regular basis.  4. Records of power have a start time and end time. In general, the time period will be
 fixed, unless record aggregation is occurring. Given the number of bits available in the format of these records, 
assume all times  are all clock times from the machine clock.  5. Distinguishing the two meters in a house: It is known 
(because the CMLC) installs them, which meter is attached to the solar panel system and which is attached to the house 
power. The mocrogrid controller for the local microgrid also knows this information. These are independent meters that 
are doing slightly different things. So, commands sent to them by the microgrid controller are specific to the 
particular destination smart meter.  I'm not sure I understand what you mean by all data being equal across both meters.
 They are measuring power flowing in different directions so their measurements will be different.  6. The isolate 
command is the way for the central utility to inform the microgrid controller or the microgrid controller to inform the 
smart meter that there is no option for power from their sources. It might be valuable (also might not matter) if the 
CMLC knows that there its batteries are exhausted and the external regional utility cables are down, that it inform the 
microgrid controllers. The same goes for the microgrid controllers informing the smart meters. You might find that they 
should be behaving differently depending on whether there is backup power available. Or you may not find that useful.  
7. Aggregation: In general, there is a desire to not lose information, so unless you find a situation in which you 
cannot store the full information locally, you should not be storing lossy-aggregated data at the expense of lossless or
 non-aggregated data. The same holds true for transmission of the data. But, until it is time to actually transmit, if 
you choose to lose some of the accuracy in stored data, you will need to justify that choice.  8. I'm not understanding 
this question. There are orthogonal states. There is the state of whether or not the external sources can provide 
auxiliary power or not (isolated or not). Separately there is the state of whether something has determined that data 
needs to be and is being aggregated. They are simply different axes. Whether or not one has the opportunity to receive 
power externally is completely separate from how/when data is being transmitted. Notice that if the microgrid is 
isolated and there is no external power, then any records for use of "purchased" power will be zero, but that does not 
mean that the metering system won't collect them. That all said, if your question was about the event log, in 16 bits 
you can store many combinations of states, so all four possibilities in this case can easily be encoded in those event 
log records.  9. See @225 and @245.  10. Good point. The figure was too simplistic. All power from the regional network 
needs to "go through" the central utility. It will be able to recharge its own batteries that way and provide power to 
the whole town system through its own connections.  11. The point of having the two sets of wires is to separate the two
 sources of power. Because the central utility will not accounting for any of the power shared within a microgrid, as 
that power leaves one house/s batteries and arrives at any of the others, it needs a separate power line that does not 
go through the smart meter for accounting. Only the power that the house is providing back to the CMLC will be counted 
for credit on the bill. In addition, for power coming into a house there are two sources that are not "counted" in 
charging them, the power from their own batteries and the power provided from the other members of their microgrid. In 
the longer run, for analysis purposes we might want to keep track of all of this, but for now, let's keep it 
straightforward. Note that the figures do not go into this level of detail. 
# @299 Recitation question
- Question: What does the layered model mean in the recitation question?
- Tags: recitation
- Students' Answer: It’s in 
lecture 8, I think it’s a network with individual layers and protocols such as the link, network, transport, and 
application layers.
- Instructors' Answer: To add just a bit more, there are many possible models for layering. What was
 mentioned above is the particular layering we use in the current Internet. Notice, for example, that in the Ethernet 
paper, they layered a file transfer protocol, which is typically an application layer protocol, directly on top of 
Ethernet, which is a link layer protocol. It doesn't really scale or generalize, but they did that. There are other 
layered models floating around as well. The point is that each layer provides additional functionality and possibly 
(probably) a different abstraction.
# @297 tsch not working in terminal?
- Question: Running ‘tsch -f’ in the athena shell yields: 'Command ‘tsch’ not found, did you mean: &nbsp; command ‘tsc’ 
from deb node-typescript &nbsp; command ‘xsch’ from deb alliance &nbsp; command ‘tcsh’ from deb tcsh &nbsp; command 
‘sch’ from deb scheme2c &nbsp; command ‘tscd’ from deb tcm Try: apt install ’ Then, tried running ‘apt install tsch’, 
‘apt-get install tsch’, ‘sudo apt-get install tsch’, ‘sudo apt install tsch’ which yielded: ‘E: Could not open lock file
 /var/lib/dpkg/lock-frontend - open (13: Permission denied) E: Unable to acquire the dpkg frontend lock 
(/var/lib/dpkg/lock-frontend), are you root?’ How do I get the terminal set up? I’m on a MacBook Pro 16’ macOS 
monterrey.
- Tags: handson2
- Students' Answer: Not sure if you properly spelled it in the Terminal and only misspelled 
it here, but the command is "tcsh -f" 
- Instructors' Answer: 
# @295 Participation check-in grades as letter grades
- Question: Despite having Canvas set to only show letter grades, some (all?) students are able to see numbers as well. 
Almost everything in this class is only given letter grades (more here). If you're seeing a number on Canvas, ignore it!

- Tags: recitation
- Students' Answer: 
- Instructors' Answer: 
# @294 How do the symbolic links in `/mit` work?
- Question: While working on the hands-on, I noticed that every time I run the command cd /mit/xxx with a new value for 
xxx (e.g. 6.033, 6.004, my kerb, etc.) and then run ls -l mit, there’s a new symbolic link added in /mit. It seems like 
cd is actually creating new links, but I was not aware that that was something it could do. What exactly is happening 
here?
- Tags: handson2
- Students' Answer: 
- Instructors' Answer: 
# @293 Questions about Link-state routing
- Question: If all nodes are sending over advertisements, would that greatly increase network congestion? How do we know
 that we are done receiving all advertisements?Dijkstra’s algorithm runs in O(N + E log N) time (E edges N nodes). What 
happens when the network has a very large N and E (for example, the internet)?  O(N + E log N) would be pretty slow. Are
 there any optimizations on this?
- Tags: lecture
- Students' Answer: 
- Instructors' Answer: 1. Yes, it does increase 
congestion! It's the main thing that prevents link-state routing from scaling.  In some sense, a node is never positive 
that it's done receiving advertisements. And in fact, we could generate networks where it never was: for instance a 
network that is constantly adding new nodes (and thus generating new advertisements). But roughly, you can imagine 
protocols proceeding like this in practice: - Collect advertisements as they come; forward copies of new advertisements 
- Every N minutes (let's say N=10), run Dijkstra's algorithm using the advertisements we've received thus far.  We'd 
expect that to do a reliable job in most networks.  2. It would be very slow! What you're going to find on Wednesday (so
 spoilers ahead) is that we run link-state routing protocols on "medium-sized" networks; think like the size of MIT's 
network. We use a hierarchy of routing protocols in order to scale up to networks like the Internet.
# @291 Lecture 9 and 10 links
- Question: Lecture 9: https://mit.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a1122d60-af3d-45be-a86d-ae4800d68e7b 
Lecture 10: https://mit.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=19926f34-f590-4ec9-ae24-ae4800d70fe9  Slides are
 (or will be) on the website, as usual.
- Tags: lecture
- Students' Answer: 
- Instructors' Answer: 
# @289 ln: failed to create symbolic link 'bineva': Read-only file system
- Question: When I tried the following command in 5.2 ln -s /afs/athena.mit.edu/user/b/i/bineva bineva I found   : ln: 
failed to create symbolic link ‘bineva’: Read-only file system Is that normal?
- Tags: handson2
- Students' Answer: See 
follow-up: @166 Maybe you are in a read-only directory, so you cannot create new files there  Also, see @178 You don't 
actually need to modify the file system here
- Instructors' Answer: 
# @288 Grep not working as expected
- Question: When i do "grep -v 'aeiou' words", i got something like the following  ... éclat éclat's élan élan's émigré 
émigré's émigrés épée épée's épées étude étude's études  It should give me all the lines that do not contain "aeiou" but
 obviously, the output has words with vows. What is the reason for this?&nbsp;
- Tags: handson2
- Students' Answer: 
resolved. 
- Instructors' Answer: 
# @287 How does the microgrid controller know the battery levels of every home?
- Question: 
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: Notice that there is a spec for those 
facts. The smart meters report the levels.
# @286 Apartments are all a part of one grid.
- Question: The spec states that all apartments are a part of the same microgrid. This means that with emergency 
services, you have ~305 residents on one microgrid. Can we make this microgrid controller send more than just 2Gb of 
data since there is such a disproportionate amount of residents?
- Tags: design_project
- Students' Answer: 
- 
Instructors' Answer: Yes, the apartments are all on one microgrid. Read the spec carefully as you think about this 
problem.
# @285 Can smart meters send data to the central utility and not just the microgrid controller?
- Question: 
- Tags: design_project
- Students' Answer: 
- Instructors' Answer: No. The smart meters talk to the 
microgrid controllers only. The microgrid controllers talk to the smart meters and the central utility.
# @284 Do we write Change Matrix jointly or individually?
- Question: Do we write Change Matrix jointly or individually?
- Tags: design_project
- Students' Answer: 
- 
Instructors' Answer: For the DP Prep assignment you are using only sections 1.1 - 1.3 of the Impact Framework. The 
change matrix is part of 1.4. That's coming later. This assignment is yours alone although you can discuss it with your 
teammates.
# @283 Outside Sources Prep Assignment
- Question: If I am using outside sources for the prep assignment, is it ok to include a footnote with the link or is 
there a best way to cite?&nbsp;  Also wanted to check if this was ok? I had some domain knowledge on the worst case 
scenario/domains affected part and I didn't want to say anything without citing.
- Tags: design_project
- Students' 
Answer: 
- Instructors' Answer: I'm not a WRAP instructor, but here's my thoughts on this. Yes, you can refer to other 
sources. For the DP Prep assignment at least, a footnote is fine. If you have outside knowledge you should need to deny 
that. so giving credit is the right thing to do.
# @281 Hands-On 2: Q4.1
- Question: Are we supposed to compare the outputs of stat . from the new directory "6.033-handson"? After creating the 
new directory and 2 new files within the new directory, my stat . output from the "6.033-handson" directory looks 
identical to before I made the 2 new files. There is no change to the number of links 
- Tags: handson2
- Students' 
Answer: 
- Instructors' Answer: stat . from “6.033-handson” means you are getting the information about the directory 
itself, and this is what we want for the question. As indicated by the question, you should be seeing a change in the 
link count after creating the directory (but not after adding a file). I’m not sure what could be going wrong so I 
suggest going to office hours or providing some more details if you are still running into this problem!
# @280 Participation Check-in #1
- Question: Your first participation check-in grades will be coming out on Canvas today, if they aren't there already 
(@279).  We release these check-in grades so that you have a sense of where you stand in terms of participation. If 
you're hoping to improve your grade, there is plenty of time to do that! Reach out to your TA and/or your recitation 
instructor; they'll be in the best position to help you improve.  Remember that we have some guidance on participation 
on the website, as well as instructions for what to do if you need to miss a recitation because of isolation. You can 
also take a look at the overall grading breakdown.
- Tags: recitation
- Students' Answer: 
- Instructors' Answer: 