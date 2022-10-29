:: This script is executed at the root folder of hive cloned project
:: after we created an Understand project with the following script
:: und create -db hive.und -languages c++ java
:: https://www.scitools.com/


for %%r in (7f9f1fcb8697fb33f0edc2c391930a3728d247d7
		e3cfeebcefe9a19c5055afdcbb00646908340694
		9265bc24d75ac945bde9ce1a0999fddd8f2aae29
		1af77bbf8356e86cabbed92cfa8cc2e1470a1d5c
		da840b0f8fa99cab9f004810cd22abc207493cae
		6f4c35c9e904d226451c465effdc5bfd31d395a0
		7590572d9265e15286628013268b2ce785c6aa08
		857a9fd8ad725a53bd95c1b2d6612f9b1155f44d
		d3fa8e0c5ac1de9f199c3df9961462d0bf819a92
		56acdd2120b9ce6790185c679223b8b5e884aaf2 
		76595628ae13b95162e77bba365fe4d2c60b3f29 
		2c2fdd524e8783f6e1f3ef15281cc2d5ed08728f 
		cb213d88304034393d68cc31a95be24f5aac62b6 
		f1e87137034e4ecbe39a859d4ef44319800016d7 
		92dd0159f440ca7863be3232f3a683a510a62b9d 
		ce61711a5fa54ab34fc74d86d521ecaeea6b072a 
		bcc7df95824831a8d2f1524e4048dfc23ab98c19 
		f4e0529634b6231a0072295da48af466cf2f10b7 
		8190d2be7b7165effa62bd21b7d60ef81fb0e4af 
		4df4d75bf1e16fe0af75aad0b4179c34c07fc975) do (
	echo New extraction started...
	git checkout %%r
	git log -1
	und settings -MetricsOutputFile E:\Documents\ETS\MGL869D\hive\undreports\metrics-%%r.csv hive.und
	und add . hive.und
	und metrics hive.und
)