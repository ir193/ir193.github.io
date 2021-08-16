Title: 记下几个奇怪的Com组件
Slug: some_interesting_com
Date: 2009-10-08 09:32:35
Tags: Security, imported blog, 
Category: Security
Author: ir193

*这是一篇导入的blog*

当时写这篇文章的原因是在写一个asp的webshell，asp的全部功能几乎都要靠ActiveX完成，所以当时几乎把系统注册表里CLASSID下的全部键值都试过了一遍，只是想找找有没有不常见的，提供合适功能的组件。最后当然是没有啦。

后来，webshell基本上写出来了，只可惜父母的电脑被学校收走了，另外一个U盘被我摔坏了，所以这个webshell未经面世就消失了，真是无比遗憾。

<!--more-->

#### 下面是导入的正文

-----------

记下几个不常见的组件，做下笔记。

1. compatUI.Util

	除了Wscript.Shell和shell.application以外，这个组件也能运行程序，但是不知道这个组件是不是系统自带的。原型是：

		Function  RunApplication(pLayers:BSTR; pszCmdLine:BSTR; bEnableLog:I4)

	使用方法：

		ocu.Runapplication "","c:\windows\system32\cmd.exe",FALSE

	我测试了一下，Xp + Netbox下确实能运行。至于参数，没查到帮助文档，不太清楚。

	这个组件还有一个比较有意思的函数CheckAdminPrivileges，看意思是检查管理员权限。

2. MakeCAB.MakeCAB

	这个组件用来打CAB包，不过好像没什么用，因为XP才带这个组件，但XP自带Zip打包功能，没人会用这个吧。想想唯一有用的是向没有压缩软件的2k系统复制东西，因为2k带expand命令，可以解压。

	以下是简单的Vbs脚本，可以将文件夹打包成CAB包

		sPath = input("请输入要打包的文件夹路径")
		sCab = input("请输入要CAB文件夹保存路径")
		set ocab=createobject("MakeCAB.MakeCAB")
		ocab.CreateCab sCAB,True,0,True
		packit sPath,""
		ocab.CloseCAB
		if NOT Err Then
			wscript.echo "打包成功"
		else
			wscript.echo "有文件没能打入压缩包"
		End if

		SUB packit(s1,s2)
			On Error Resume next
			if Right(s1,1) &lt;&gt; "\" s1=s1 &amp; "\"
			if Right(s2,1) &lt;&gt; "" s2=s2 &amp; "\"
			'注释:S1文件路径,S2在CAB包内的路径
			set ofso=createobject("Scripting.FileSystemObject")
			if ofso.FolderExists(s1) then
				set ofolder=ofso.GetFolder(s1)
				For each oSubfolder in ofolder.Subfolders
					packit s1 &amp; oSubfolder.Name,s2 &amp; oSubfolder.Name
					'递归遍历文件夹
				Next
				For each oFile in ofolder.Files
					ocab.AddFile s1 &amp; oFile.Name,s2 &amp; oFile.Name
				Next
			End if
		End SUB

		需要解压时，RAR就能打开。没有RAR，可以使用：`Expand "filepath" F:*.* outpath`

3. WinHTTPRequest.WinHTTPRequest

	这个组件好像很重要，因为这个DLL总是在使用。功能和XMLHttp差不多，不同的是可以设置连接超时。具体用法和XMLhttp差不多

4. SAFRCFileDlg.FileOpen 和 UserAccounts.CommonDialog

	这个用来创建打开文件对话框。类似的还有UserAccounts.CommonDialog，这个功能更强大。

		* SAFRCFileDlg.FileSave对象：属性有：

			FileName — 指定默认文件名；
			FileType — 指定文件扩展名；
			OpenFileSaveDlg — 显示文件保存框体方法。

		* SAFRCFileDlg.FileOpen 对象：

			FileName — 默认文件名属性；
			OpenFileOpenDlg — 显示打开文件框体方法。
		
		* UserAccounts.CommonDialog对象：

			Filter — 扩展名属性（"vbs File|*.vbs|All Files|*.*"）；<
			FilterIndex — 指定
			InitialDir — 指定默认的文件夹
			FileName — 指定的文件名
			Flags — 对话框的类型
			Showopen — 显示：


5. SAPI.SpVoice

	这个有点意思，可以语音读文字。一个例子：

		SzBuf = InputBox( "输入英文", "输入", "I LOVE YOU" )
		set tack=CreateObject("SAPI.SpVoice")
		tack.Speak(SzBuf)

6. agent.control

	这个也有点意思，用来产生一个officeXP那样的小助手。一个例子：

		AgentControl=createobject("agent.control")
		AgentControl.Connected = True
		AgentControl.Characters.Load "Merlin", "Merlin.acs"
		Set Merlin = AgentControl.Characters("Merlin")
		Merlin.Get "State", "Showing, Speaking"
		Merlin.Get "Animation", "Greet, GreetReturn"
		Merlin.Show
		Merlin.Get "State", "Hiding"
		Merlin.Play "Greet"  '这个让他鞠躬
		Merlin.Speak "hello"  '这个让他说话
		Merlin.Play "Greet"
		wscript.sleep 5000
		Merlin.Speak "welcome "
		Merlin.Play "Greet"
		wscript.sleep 5000
		Merlin.Speak "goodbay"
		wscript.sleep 5000
		Merlin.Hide

