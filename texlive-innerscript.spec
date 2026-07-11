%global tl_name innerscript
%global tl_revision 75161

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4a
Release:	%{tl_revision}.1
Summary:	Small modifications to math formatting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/innerscript
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/innerscript.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/innerscript.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/innerscript.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package optionally modifies four aspects of TeX's automatic math
formatting to improve typesetting: (1) it adds extra space around
relation and operation symbols in superscripts and subscripts; (2) it
removes extra space around \left-\right delimiter pairs; (3) it adds
extra space after right delimiters in certain situations; and (4) it
forces \left and \right delimiters to completely cover their contents.
Using LuaLaTeX is required.

