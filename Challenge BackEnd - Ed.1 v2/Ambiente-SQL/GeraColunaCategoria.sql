alter table cbe.EnderecosVideos
	add categoriaId int
go

-- Seguindo regra de neg�cio: caso o v�deo n�o possua categoria, ent�o inclu�mos a refer�ncia ao Id = 1 (livre)
update cbe.EnderecosVideos
	set categoriaId = 1 where categoriaId is null