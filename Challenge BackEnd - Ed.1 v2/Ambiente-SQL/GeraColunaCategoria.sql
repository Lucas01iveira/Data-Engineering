alter table cbe.EnderecosVideos
	add categoriaId int
go

-- Seguindo regra de negócio: caso o vídeo não possua categoria, então incluímos a referência ao Id = 1 (livre)
update cbe.EnderecosVideos
	set categoriaId = 1 where categoriaId is null