%global tl_name bangorcsthesis
%global tl_revision 75154

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.5.7
Release:	%{tl_revision}.1
Summary:	Typeset a thesis at Bangor University
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bangorcsthesis
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bangorcsthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bangorcsthesis.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bangorcsthesis.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class typesets thesis/dissertation documents for all levels (i.e.,
both undergraduate and graduate students may use the class). It also
provides macros designed to optimise the process of producing a thesis.

