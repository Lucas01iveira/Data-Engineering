drop table if exists cbe.EnderecosVideos
go

create table cbe.EnderecosVideos 
(
	Id int not null identity(1,1)
	,Titulo varchar(1000)
	,Descricao varchar(1000) 
	,Url varchar(1000) not null
)
