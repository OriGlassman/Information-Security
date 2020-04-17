   0xb7c81ca0 <+0>:	push   ebp
   0xb7c81ca1 <+1>:	mov    ebp,esp
   0xb7c81ca3 <+3>:	push   edi
   0xb7c81ca4 <+4>:	push   esi
   0xb7c81ca5 <+5>:	push   ebx
   0xb7c81ca6 <+6>:	call   0xb7d41b55 <__x86.get_pc_thunk.bx>
   0xb7c81cab <+11>:	add    ebx,0x152355
   0xb7c81cb1 <+17>:	sub    esp,0x28
   0xb7c81cb4 <+20>:	push   DWORD PTR [ebp+0x8]
   0xb7c81cb7 <+23>:	call   0xb7c975c0 <__strlen_ia32>
   0xb7c81cbc <+28>:	mov    edx,DWORD PTR [ebx+0xdfc]
   0xb7c81cc2 <+34>:	mov    esi,eax
   0xb7c81cc4 <+36>:	add    esp,0x10
   0xb7c81cc7 <+39>:	mov    eax,DWORD PTR [edx]
   0xb7c81cc9 <+41>:	mov    DWORD PTR [ebp-0x1c],edx
   0xb7c81ccc <+44>:	and    eax,0x8000
   0xb7c81cd1 <+49>:	mov    DWORD PTR [ebp-0x20],eax
   0xb7c81cd4 <+52>:	jne    0xb7c81d1e <_IO_puts+126>
   0xb7c81cd6 <+54>:	mov    ecx,DWORD PTR [edx+0x48]
   0xb7c81cd9 <+57>:	mov    edi,DWORD PTR gs:0x8
   0xb7c81ce0 <+64>:	mov    eax,edi
   0xb7c81ce2 <+66>:	cmp    eax,DWORD PTR [ecx+0x8]
   0xb7c81ce5 <+69>:	mov    edi,ecx
   0xb7c81ce7 <+71>:	mov    DWORD PTR [ebp-0x24],eax
   0xb7c81cea <+74>:	je     0xb7c81d1a <_IO_puts+122>
   0xb7c81cec <+76>:	mov    eax,DWORD PTR [ebp-0x20]
   0xb7c81cef <+79>:	mov    ecx,0x1
   0xb7c81cf4 <+84>:	cmp    DWORD PTR gs:0xc,0x0
   0xb7c81cfc <+92>:	je     0xb7c81cff <_IO_puts+95>
   0xb7c81cfe <+94>:	lock cmpxchg DWORD PTR [edi],ecx
   0xb7c81d02 <+98>:	je     0xb7c81d0b <_IO_puts+107>
   0xb7c81d04 <+100>:	lea    ecx,[edi]
   0xb7c81d06 <+102>:	call   0xb7d15b40 <__lll_lock_wait_private>
   0xb7c81d0b <+107>:	mov    ecx,DWORD PTR [edx+0x48]
   0xb7c81d0e <+110>:	mov    eax,DWORD PTR [ebp-0x24]
   0xb7c81d11 <+113>:	mov    edx,DWORD PTR [ebx+0xdfc]
   0xb7c81d17 <+119>:	mov    DWORD PTR [ecx+0x8],eax
   0xb7c81d1a <+122>:	add    DWORD PTR [ecx+0x4],0x1
   0xb7c81d1e <+126>:	movsx  eax,BYTE PTR [edx+0x46]
   0xb7c81d22 <+130>:	test   al,al
   0xb7c81d24 <+132>:	jne    0xb7c81d4e <_IO_puts+174>
   0xb7c81d26 <+134>:	mov    eax,DWORD PTR [ebx-0xf4]
   0xb7c81d2c <+140>:	test   eax,eax
   0xb7c81d2e <+142>:	je     0xb7c81e20 <_IO_puts+384>
   0xb7c81d34 <+148>:	mov    eax,DWORD PTR [edx+0x68]
---Type <return> to continue, or q <return> to quit---
   0xb7c81d37 <+151>:	test   eax,eax
   0xb7c81d39 <+153>:	je     0xb7c81da8 <_IO_puts+264>
   0xb7c81d3b <+155>:	cmp    eax,0xffffffff
   0xb7c81d3e <+158>:	jne    0xb7c81e10 <_IO_puts+368>
   0xb7c81d44 <+164>:	mov    edx,DWORD PTR [ebx+0xdfc]
   0xb7c81d4a <+170>:	movsx  eax,BYTE PTR [edx+0x46]
   0xb7c81d4e <+174>:	mov    eax,DWORD PTR [edx+eax*1+0x94]
   0xb7c81d55 <+181>:	sub    esp,0x4
   0xb7c81d58 <+184>:	push   esi
   0xb7c81d59 <+185>:	push   DWORD PTR [ebp+0x8]
   0xb7c81d5c <+188>:	push   edx
   0xb7c81d5d <+189>:	call   DWORD PTR [eax+0x1c]
   0xb7c81d60 <+192>:	add    esp,0x10
   0xb7c81d63 <+195>:	cmp    esi,eax
   0xb7c81d65 <+197>:	jne    0xb7c81e10 <_IO_puts+368>
   0xb7c81d6b <+203>:	mov    eax,DWORD PTR [ebx+0xdfc]
   0xb7c81d71 <+209>:	mov    edx,DWORD PTR [eax+0x14]
   0xb7c81d74 <+212>:	cmp    edx,DWORD PTR [eax+0x18]
   0xb7c81d77 <+215>:	jae    0xb7c81df0 <_IO_puts+336>
   0xb7c81d79 <+217>:	lea    ecx,[edx+0x1]
   0xb7c81d7c <+220>:	mov    DWORD PTR [eax+0x14],ecx
   0xb7c81d7f <+223>:	mov    BYTE PTR [edx],0xa
   0xb7c81d82 <+226>:	add    esi,0x1
   0xb7c81d85 <+229>:	mov    eax,0x7fffffff
   0xb7c81d8a <+234>:	cmovs  esi,eax
   0xb7c81d8d <+237>:	mov    eax,DWORD PTR [ebp-0x1c]
   0xb7c81d90 <+240>:	test   DWORD PTR [eax],0x8000
   0xb7c81d96 <+246>:	je     0xb7c81db8 <_IO_puts+280>
   0xb7c81d98 <+248>:	lea    esp,[ebp-0xc]
   0xb7c81d9b <+251>:	mov    eax,esi
   0xb7c81d9d <+253>:	pop    ebx
   0xb7c81d9e <+254>:	pop    esi
   0xb7c81d9f <+255>:	pop    edi
   0xb7c81da0 <+256>:	pop    ebp
   0xb7c81da1 <+257>:	ret    
   0xb7c81da2 <+258>:	lea    esi,[esi+0x0]
   0xb7c81da8 <+264>:	mov    DWORD PTR [edx+0x68],0xffffffff
   0xb7c81daf <+271>:	jmp    0xb7c81d4a <_IO_puts+170>
   0xb7c81db1 <+273>:	lea    esi,[esi+eiz*1+0x0]
   0xb7c81db8 <+280>:	mov    eax,DWORD PTR [ebp-0x1c]
   0xb7c81dbb <+283>:	mov    edx,DWORD PTR [eax+0x48]
   0xb7c81dbe <+286>:	sub    DWORD PTR [edx+0x4],0x1
   0xb7c81dc2 <+290>:	jne    0xb7c81d98 <_IO_puts+248>
   0xb7c81dc4 <+292>:	mov    DWORD PTR [edx+0x8],0x0
   0xb7c81dcb <+299>:	cmp    DWORD PTR gs:0xc,0x0
   0xb7c81dd3 <+307>:	je     0xb7c81dd6 <_IO_puts+310>
---Type <return> to continue, or q <return> to quit---
   0xb7c81dd5 <+309>:	lock sub DWORD PTR [edx],0x1
   0xb7c81dd9 <+313>:	je     0xb7c81de2 <_IO_puts+322>
   0xb7c81ddb <+315>:	lea    eax,[edx]
   0xb7c81ddd <+317>:	call   0xb7d15b70 <__lll_unlock_wake_private>
   0xb7c81de2 <+322>:	lea    esp,[ebp-0xc]
   0xb7c81de5 <+325>:	mov    eax,esi
   0xb7c81de7 <+327>:	pop    ebx
   0xb7c81de8 <+328>:	pop    esi
   0xb7c81de9 <+329>:	pop    edi
   0xb7c81dea <+330>:	pop    ebp
   0xb7c81deb <+331>:	ret    
   0xb7c81dec <+332>:	lea    esi,[esi+eiz*1+0x0]
   0xb7c81df0 <+336>:	sub    esp,0x8
   0xb7c81df3 <+339>:	push   0xa
   0xb7c81df5 <+341>:	push   eax
   0xb7c81df6 <+342>:	call   0xb7c8cdd0 <__GI___overflow>
   0xb7c81dfb <+347>:	add    esp,0x10
   0xb7c81dfe <+350>:	cmp    eax,0xffffffff
   0xb7c81e01 <+353>:	jne    0xb7c81d82 <_IO_puts+226>
   0xb7c81e07 <+359>:	mov    esi,esi
   0xb7c81e09 <+361>:	lea    edi,[edi+eiz*1+0x0]
   0xb7c81e10 <+368>:	mov    esi,0xffffffff
   0xb7c81e15 <+373>:	jmp    0xb7c81d8d <_IO_puts+237>
   0xb7c81e1a <+378>:	lea    esi,[esi+0x0]
   0xb7c81e20 <+384>:	sub    esp,0x8
   0xb7c81e23 <+387>:	push   0xffffffff
   0xb7c81e25 <+389>:	push   edx
   0xb7c81e26 <+390>:	call   0xb7c86e00 <_IO_fwide>
   0xb7c81e2b <+395>:	add    esp,0x10
   0xb7c81e2e <+398>:	jmp    0xb7c81d3b <_IO_puts+155>
   0xb7c81e33 <+403>:	mov    ecx,eax
   0xb7c81e35 <+405>:	mov    eax,DWORD PTR [ebp-0x1c]
   0xb7c81e38 <+408>:	test   DWORD PTR [eax],0x8000
   0xb7c81e3e <+414>:	jne    0xb7c81e67 <_IO_puts+455>
   0xb7c81e40 <+416>:	mov    edx,DWORD PTR [eax+0x48]
   0xb7c81e43 <+419>:	sub    DWORD PTR [edx+0x4],0x1
   0xb7c81e47 <+423>:	jne    0xb7c81e67 <_IO_puts+455>
   0xb7c81e49 <+425>:	mov    DWORD PTR [edx+0x8],0x0
   0xb7c81e50 <+432>:	cmp    DWORD PTR gs:0xc,0x0
   0xb7c81e58 <+440>:	je     0xb7c81e5b <_IO_puts+443>
   0xb7c81e5a <+442>:	lock sub DWORD PTR [edx],0x1
   0xb7c81e5e <+446>:	je     0xb7c81e67 <_IO_puts+455>
   0xb7c81e60 <+448>:	lea    eax,[edx]
   0xb7c81e62 <+450>:	call   0xb7d15b70 <__lll_unlock_wake_private>
   0xb7c81e67 <+455>:	sub    esp,0xc
   0xb7c81e6a <+458>:	push   ecx
