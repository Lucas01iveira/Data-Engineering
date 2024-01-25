alter table cbe.EnderecosVideos
	add CategoriaId int
go

-- Seguindo regra de negócio: caso o vídeo não possua categoria, então incluímos a referência ao Id = 1 (livre)
update cbe.EnderecosVideos
	set CategoriaId = 1 where CategoriaId is null