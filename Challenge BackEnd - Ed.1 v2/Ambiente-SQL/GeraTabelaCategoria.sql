drop table if exists cbe.Categoria
go

create table cbe.Categoria
(
	Id int not null identity(1,1)
	,DescricaoCategoria varchar(50)
	,Cor varchar(50)
)
go

alter table cbe.Categoria
	add constraint Pk_Id primary key (Id)