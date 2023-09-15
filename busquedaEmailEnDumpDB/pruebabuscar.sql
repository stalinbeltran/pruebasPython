USE [SES]
GO
/****** Object:  Table [dbo].[Adjuntos]    Script Date: 26/07/23 1:45:51 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Adjuntos](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[Solicitudes_id] [int] NULL,
	[nombreArchivo] [nvarchar](500) NULL,
	[envioID] [nvarchar](80) NULL,
	[usuario] [nvarchar](80) NULL,
	[fecha] [datetime] NULL,
 CONSTRAINT [PK_Adjuntos] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[AdjuntosCodigo]    Script Date: 26/07/23 1:45:51 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AdjuntosCodigo](
	[id] [bigint] IDENTITY(1,1) NOT NULL,
	[solicitudid] [int] NOT NULL,
	[nombre] [nvarchar](max) NULL,
	[codigomd5] [nvarchar](max) NULL,
	[fecha] [datetime] NULL,
	[usuario] [nvarchar](max) NULL,
 CONSTRAINT [PK_AdjuntosCodigo] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[AnuncioEstados]    Script Date: 26/07/23 1:45:51 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AnuncioEstados](
	[AnuncioEstadoId] [int] IDENTITY(1,1) NOT NULL,
	[AnuncioId] [int] NOT NULL,
	[Usuario] [nvarchar](100) NULL,
	[Estado] [bit] NOT NULL,
	[FechaModificacion] [datetime] NOT NULL,
 CONSTRAINT [PK_AnuncioEstados] PRIMARY KEY CLUSTERED 
(
	[AnuncioEstadoId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Anuncios]    Script Date: 26/07/23 1:45:51 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Anuncios](
	[AnuncioId] [int] IDENTITY(1,1) NOT NULL,
	[Titulo] [nvarchar](200) NOT NULL,
	[Descripcion] [nvarchar](max) NOT NULL,
	[Estado] [bit] NOT NULL,
	[tipo] [int] NOT NULL,
	[FechaCreacion] [datetime] NOT NULL,
	[FechaVencimiento] [datetime] NOT NULL,
	[CreadoPor] [nvarchar](100) NULL,
 CONSTRAINT [PK_Anuncios] PRIMARY KEY CLUSTERED 
(