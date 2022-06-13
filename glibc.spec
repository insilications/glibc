#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : glibc
Version  : 2.35
Release  : 1518
URL      : file:///insilications/apps/glibc-2.35.tar.gz
Source0  : file:///insilications/apps/glibc-2.35.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: clr-systemd-config-data
Requires: filesystem
Requires: nss-altfiles-lib
BuildRequires : bison
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gettext
BuildRequires : gettext-dev
BuildRequires : grep
BuildRequires : libgcc1
BuildRequires : libstdc++
BuildRequires : linux-libc-headers
BuildRequires : python3-dev
BuildRequires : texinfo
BuildRequires : util-linux
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Set-host.conf-multi-to-on-by-default.patch
Patch2: 0001-sysdeps-unix-Add-support-for-usr-lib32-as-a-system-l.patch
Patch3: ld-so-cache-in-var.patch
Patch4: mkdir-ldconfig.patch
Patch5: locale-var-cache.patch
Patch6: nonscd.patch
Patch7: alternate_trim.patch
Patch8: tzselect-proper-zone-file.patch
Patch9: malloc_tune.patch
Patch10: 0001-misc-Support-fallback-stateless-shells-path-in-absen.patch
Patch11: stateless.patch
Patch12: mathlto.patch
Patch13: vzeroupper-2.27.patch
Patch14: pause.patch
Patch15: spin-smarter.patch
Patch16: nostackshrink.patch
Patch17: 0001-Set-vector-width-and-alignment-to-fix-GCC-AVX-issue.patch
Patch18: disable-vectorization-even-more.patch
Patch19: 0001-Force-ffsll-to-be-64-bytes-aligned.patch
Patch20: utf8-locale-naming.patch
Patch21: noclone3yet.patch
Patch22: seccomp_workaround.patch
Patch23: nsswitch.patch
Patch24: 0001-modify-no-pie-ccflag.patch

%description
No detailed description available

%prep
%setup -q -n glibc-2.35
cd %{_builddir}/glibc-2.35
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
pushd %{_builddir}
cp -a %{_builddir}/glibc-2.35 build32
popd
pushd %{_builddir}
cp -a %{_builddir}/glibc-2.35 build-special
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1655135269
## altflags1f content
## altflags1
export ASFLAGS="-D__AVX__=1 -D__AVX2__=1 -msse2avx -D__FMA__=1 -DNDEBUG=1"
export CFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -fno-semantic-interposition -mno-direct-extern-access -fno-pic -fno-PIC -fno-plt -Wl,-Bsymbolic-functions -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export ASMFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -fno-semantic-interposition -mno-direct-extern-access -fno-pic -fno-PIC -fno-plt -Wl,-Bsymbolic-functions -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export CXXFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -fno-semantic-interposition -mno-direct-extern-access -fno-pic -fno-PIC -fno-plt -Wl,-Bsymbolic-functions -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -fvisibility-inlines-hidden -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wno-inline -Wall -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export FCFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -fno-semantic-interposition -mno-direct-extern-access -fno-pic -fno-PIC -fno-plt -Wl,-Bsymbolic-functions -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export FFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -fno-semantic-interposition -mno-direct-extern-access -fno-pic -fno-PIC -fno-plt -Wl,-Bsymbolic-functions -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export LDFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -fno-semantic-interposition -mno-direct-extern-access -fno-pic -fno-PIC -fno-plt -Wl,-Bsymbolic-functions -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
%global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
# export CPATH=/usr/include
# export LIBRARY_PATH=%{_libdir}
# export PATH="/usr/bin/haswell:/usr/bin:/usr/sbin"
## altflags1f end
# Keep only the UTF-8 locales...
supported=./localedata/SUPPORTED
sed -nr '/^(#|SUPPORTED-LOCALES=|.*\/UTF-8)/p' $supported > $supported.new
mv -v $supported.new $supported

if [ ! -d "glibc-build" ]; then
    mkdir glibc-build;
fi


pushd glibc-build/
../configure \
    --prefix=/usr \
    --exec_prefix=/usr \
    --bindir=/usr/bin \
    --sbindir=/usr/bin \
    --libexecdir=/usr/lib64/glibc \
    --datadir=/usr/share \
    --sysconfdir=%{_sysconfdir} \
    --sharedstatedir=%{_localstatedir}/lib \
    --localstatedir=%{_localstatedir} \
    --libdir=/usr/lib64 \
    --localedir=/usr/share/locale \
    --infodir=/usr/share/info \
    --mandir=/usr/share/man \
    --disable-silent-rules \
    --disable-dependency-tracking \
    --enable-kernel=3.10 \
    --without-cvs \
    --disable-profile \
    --disable-debug \
    --without-gd \
    --enable-clocale=gnu \
    --enable-add-ons \
    --without-selinux \
    --enable-obsolete-rpc \
    --with-pkgversion='Clear Linux Software for Intel Architecture' \
    --enable-lock-elision=yes \
    --enable-bind-now \
    --enable-tunables \
    --enable-stack-protector=no \
    --disable-stack-protector \
    --enable-obsolete-nsl \
    --disable-cet \
    --disable-static-pie \
    --disable-default-pie \
    --disable-werror \
    --enable-mathvec \
    --disable-multi-arch \
    --with-nonshared-cflags="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -fno-semantic-interposition -mno-direct-extern-access -fno-pic -fno-PIC -fno-plt -Wl,-Bsymbolic-functions -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000" \
    libc_cv_slibdir=/usr/lib64 \
    libc_cv_complocaledir=/usr/share/locale
## make_macro content
make -O -j16 V=1
make USE_CLOCK_GETTIME=1 bench-build -j16
popd
## make_macro end

pushd ../build-special/
## altflags1_special content
## altflags1
export ASFLAGS="-D__AVX__=1 -D__AVX2__=1 -msse2avx -D__FMA__=1 -DNDEBUG=1"
export CFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export ASMFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export CXXFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -fvisibility-inlines-hidden -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wno-inline -Wall -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export FCFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export FFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export LDFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
%global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
# export CPATH=/usr/include
# export LIBRARY_PATH=%{_libdir}
# export PATH="/usr/bin/haswell:/usr/bin:/usr/sbin"
## altflags1_special end
if [ ! -d "glibc-build-shared" ]; then
    mkdir glibc-build-shared;
fi

pushd glibc-build-shared/
../configure \
    --prefix=/usr \
    --exec_prefix=/usr \
    --bindir=/usr/bin \
    --sbindir=/usr/bin \
    --libexecdir=/usr/lib64/glibc \
    --datadir=/usr/share \
    --sysconfdir=%{_sysconfdir} \
    --sharedstatedir=%{_localstatedir}/lib \
    --localstatedir=%{_localstatedir} \
    --libdir=/usr/lib64 \
    --localedir=/usr/share/locale \
    --infodir=/usr/share/info \
    --mandir=/usr/share/man \
    --disable-silent-rules \
    --disable-dependency-tracking \
    --enable-kernel=3.10 \
    --without-cvs \
    --disable-profile \
    --disable-debug \
    --without-gd \
    --enable-clocale=gnu \
    --enable-add-ons \
    --without-selinux \
    --enable-obsolete-rpc \
    --with-pkgversion='Clear Linux Software for Intel Architecture' \
    --enable-lock-elision=yes \
    --enable-bind-now \
    --enable-tunables \
    --enable-stack-protector=no \
    --disable-stack-protector \
    --enable-obsolete-nsl \
    --disable-cet \
    --disable-static-pie \
    --disable-default-pie \
    --disable-werror \
    --enable-mathvec \
    --disable-multi-arch \
    --with-nonshared-cflags="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000" \
    libc_cv_slibdir=/usr/lib64 \
    libc_cv_complocaledir=/usr/share/locale
## make_macro_special content
make -O -j16 V=1

popd
## make_macro_special end
popd
pushd ../build32/
## altflags1_32 content
unset CFLAGS
unset CXXFLAGS
unset FCFLAGS
unset FFLAGS
unset LDFLAGS
unset LINKFLAGS
unset ASFLAGS
unset LD_LIBRARY_PATH
unset LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export CFLAGS="-O3 -m32 -march=skylake -mtune=skylake -mstackrealign -Wl,-z,max-page-size=0x1000 -pipe"
export FCFLAGS="-O3 -m32 -march=skylake -mtune=skylake -mstackrealign -Wl,-z,max-page-size=0x1000 -pipe"
export FFLAGS="-O3 -m32 -march=skylake -mtune=skylake -mstackrealign -Wl,-z,max-page-size=0x1000 -pipe"
export CXXFLAGS="-O3 -m32 -march=skylake -mtune=skylake -mstackrealign -Wl,-z,max-page-size=0x1000 -pipe"
export LDFLAGS="-O3 -m32 -march=skylake -mtune=skylake -mstackrealign -Wl,-z,max-page-size=0x1000 -pipe"
export ASMFLAGS="-O3 -m32 -march=skylake -mtune=skylake -mstackrealign -Wl,-z,max-page-size=0x1000 -pipe"
unset ASFLAGS
# export ASFLAGS="--32"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
%global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/lib64/pkgconfig:/usr/share/pkgconfig"
unset CPATH
unset LIBRARY_PATH
# export PATH="/usr/bin/haswell:/usr/bin:/usr/sbin"
## altflags1_32 end
if [ ! -d "glibc-build32" ]; then
    mkdir glibc-build32;
fi

pushd glibc-build32/
../configure \
    --prefix=/usr \
    --exec_prefix=/usr \
    --bindir=/usr/bin \
    --sbindir=/usr/bin \
    --libexecdir=/usr/lib32/glibc \
    --datadir=/usr/share \
    --sysconfdir=%{_sysconfdir} \
    --sharedstatedir=%{_localstatedir}/lib \
    --localstatedir=%{_localstatedir} \
    --libdir=/usr/lib32 \
    --localedir=/usr/share/locale \
    --infodir=/usr/share/info \
    --mandir=/usr/share/man \
    --disable-silent-rules \
    --disable-dependency-tracking \
    --enable-kernel=3.10 \
    --without-cvs \
    --disable-profile \
    --disable-debug \
    --without-gd \
    --enable-clocale=gnu \
    --enable-add-ons \
    --without-selinux \
    --enable-obsolete-rpc \
    --build=i686-generic-linux \
    --host=i686-linux-gnu \
    --target=i686-generic-linux \
    --with-pkgversion='Clear Linux Software for Intel Architecture' \
    --enable-lock-elision=yes \
    --enable-bind-now \
    --enable-tunables \
    --disable-stack-protector \
    --enable-obsolete-nsl \
    --disable-cet \
    --disable-static-pie \
    --disable-default-pie \
    --disable-werror \
    libc_cv_slibdir=/usr/lib32 \
    libc_cv_complocaledir=/usr/share/locale \
    libc_cv_can_use_register_asm_ebp=no \
    CC="gcc -m32" CXX="g++ -m32" i686-linux-gnu
## make_macro_32 content
make -O -j16 V=1

popd
## make_macro_32 end
popd

%install
export SOURCE_DATE_EPOCH=1655135269
rm -rf %{buildroot}
## altflags1_32 content
unset CFLAGS
unset CXXFLAGS
unset FCFLAGS
unset FFLAGS
unset LDFLAGS
unset LINKFLAGS
unset ASFLAGS
unset LD_LIBRARY_PATH
unset LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export CFLAGS="-O3 -m32 -march=skylake -mtune=skylake -mstackrealign -Wl,-z,max-page-size=0x1000 -pipe"
export FCFLAGS="-O3 -m32 -march=skylake -mtune=skylake -mstackrealign -Wl,-z,max-page-size=0x1000 -pipe"
export FFLAGS="-O3 -m32 -march=skylake -mtune=skylake -mstackrealign -Wl,-z,max-page-size=0x1000 -pipe"
export CXXFLAGS="-O3 -m32 -march=skylake -mtune=skylake -mstackrealign -Wl,-z,max-page-size=0x1000 -pipe"
export LDFLAGS="-O3 -m32 -march=skylake -mtune=skylake -mstackrealign -Wl,-z,max-page-size=0x1000 -pipe"
export ASMFLAGS="-O3 -m32 -march=skylake -mtune=skylake -mstackrealign -Wl,-z,max-page-size=0x1000 -pipe"
unset ASFLAGS
# export ASFLAGS="--32"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
%global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/lib64/pkgconfig:/usr/share/pkgconfig"
unset CPATH
unset LIBRARY_PATH
# export PATH="/usr/bin/haswell:/usr/bin:/usr/sbin"
## altflags1_32 end
## install_macro_32 start
pushd ../build32/
pushd glibc-build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
    pushd %{buildroot}/usr/lib32/pkgconfig
    for i in *.pc ; do ln -s $i 32$i ; done
    popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
    pushd %{buildroot}/usr/share/pkgconfig
    for i in *.pc ; do ln -s $i 32$i ; done
    popd
fi
popd
popd
## install_macro_32 end
## altflags1_special content
## altflags1
export ASFLAGS="-D__AVX__=1 -D__AVX2__=1 -msse2avx -D__FMA__=1 -DNDEBUG=1"
export CFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export ASMFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export CXXFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -fvisibility-inlines-hidden -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wno-inline -Wall -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export FCFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export FFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export LDFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
%global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
# export CPATH=/usr/include
# export LIBRARY_PATH=%{_libdir}
# export PATH="/usr/bin/haswell:/usr/bin:/usr/sbin"
## altflags1_special end
## install_macro_build_special start
# install_macro_build_special
pushd ../build-special/
pushd glibc-build-shared/
%make_install_special
mkdir -p %{buildroot}/usr/lib64/haswell
cp math/libm.so %{buildroot}/usr/lib64/haswell/libm.so.6
cp mathvec/libmvec.so %{buildroot}/usr/lib64/haswell/libmvec.so.1
cp crypt/libcrypt.so %{buildroot}/usr/lib64/haswell/libcrypt.so.1
cp libc.so  %{buildroot}/usr/lib64/haswell/libc.so.6
popd
popd
## install_macro_build_special end
## altflags1f content
## altflags1
export ASFLAGS="-D__AVX__=1 -D__AVX2__=1 -msse2avx -D__FMA__=1 -DNDEBUG=1"
export CFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -fno-semantic-interposition -mno-direct-extern-access -fno-pic -fno-PIC -fno-plt -Wl,-Bsymbolic-functions -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export ASMFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -fno-semantic-interposition -mno-direct-extern-access -fno-pic -fno-PIC -fno-plt -Wl,-Bsymbolic-functions -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export CXXFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -fno-semantic-interposition -mno-direct-extern-access -fno-pic -fno-PIC -fno-plt -Wl,-Bsymbolic-functions -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -fvisibility-inlines-hidden -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wno-inline -Wall -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export FCFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -fno-semantic-interposition -mno-direct-extern-access -fno-pic -fno-PIC -fno-plt -Wl,-Bsymbolic-functions -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export FFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -fno-semantic-interposition -mno-direct-extern-access -fno-pic -fno-PIC -fno-plt -Wl,-Bsymbolic-functions -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export LDFLAGS="-Wa,-mrelax-relocations=yes -DNDEBUG=1 -m64 -D__AVX2__=1 -D__AVX__=1 -D__FMA__=1 -O3 -fno-semantic-interposition -mno-direct-extern-access -fno-pic -fno-PIC -fno-plt -Wl,-Bsymbolic-functions -falign-functions=32 -ffat-lto-objects -flive-range-shrinkage -fno-lto -fno-reorder-blocks-and-partition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -g3 -grecord-gcc-switches -gdescribe-dies -malign-data=cacheline -march=native -mavx -mavx2 -mno-vzeroupper -mprefer-vector-width=256 -mrelax-cmpxchg-loop -msse2avx -mtune=native -pipe -Wall -Wno-inline -Wl,--build-id=sha1 -Wl,--emit-relocs -Wl,-O2 -Wl,-z,max-page-size=0x1000"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
%global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
# export CPATH=/usr/include
# export LIBRARY_PATH=%{_libdir}
# export PATH="/usr/bin/haswell:/usr/bin:/usr/sbin"
## altflags1f end
## install_macro start
pushd glibc-build/
%make_install
mkdir -p %{buildroot}/usr/lib64/haswell
cp math/libm.so %{buildroot}/usr/lib64/haswell/libm.so.6
cp mathvec/libmvec.so %{buildroot}/usr/lib64/haswell/libmvec.so.1
cp crypt/libcrypt.so %{buildroot}/usr/lib64/haswell/libcrypt.so.1
cp libc.so  %{buildroot}/usr/lib64/haswell/libc.so.6
## install_macro end
## install_append content
mkdir -p %{buildroot}/var/cache/locale

# FIXME: As of glibc 2.35, the --prefix flag to iconvconfig appears to behave
# differently, since it hardcodes the prefix path to the cache's module lookup
# path, which in turn breaks iconv completely (unless GCONV_PATH is set in the
# environment). Once that issue is resolved (or another BKM is found),
# re-enable the cache by running the iconvconfig command below. The cache
# improves performance of iconv, so we want it to be enabled...
# Upstream report to track:
# https://sourceware.org/bugzilla/show_bug.cgi?id=28199
rm -fv %{buildroot}/usr/lib64/gconv/gconv-modules.cache
#iconvconfig --prefix=%{buildroot}


make -s -O localedata/install-locales  DESTDIR=%{buildroot} install_root=%{buildroot} -j14

# Make ldconfig not fail
install -d %{buildroot}/var/cache/ldconfig

install -d %{buildroot}%{_datadir}/defaults/etc/
mv %{buildroot}%{_sysconfdir}/rpc %{buildroot}%{_datadir}/defaults/etc/rpc

mkdir -p %{buildroot}/usr/lib64/glibc/benchmarks
for f in benchtests/*; do [ -x $f -a ! -d $f ] && cp -a $f %{buildroot}/usr/lib64/glibc/benchmarks; done
pushd %{buildroot}/usr/bin
find ../lib64/glibc/benchmarks -type f -exec ln -s {} . \;
popd

## Generate UTF-8 locale-related data
make -s -O -j14 localedata/install-locale-files DESTDIR=%{buildroot} install_root=%{buildroot}
for origpath in %{buildroot}/usr/share/locale/*.utf8*; do
  rename -v .utf8 .UTF-8 "$origpath"
done

# Reduce footprint of localedata, since `make localedata/install-locale-files`
# passes the `--no-hard-links` option to `localedef`.
hardlink %{buildroot}/usr/share/locale

# ../glibc-build
popd

ln -sfv /var/cache/locale/locale-archive %{buildroot}/usr/share/locale/locale-archive

mkdir -p %{buildroot}/usr/lib
ln -s ../lib32/ld-linux.so.2  %{buildroot}/usr/lib/ld-linux.so.2

# for oracle db installer (compat link)
ln -sf libpthread.a %{buildroot}/usr/lib64/libpthread_nonshared.a

# Get things out of /sbin and /usr/sbin
mv %{buildroot}/sbin/sln %{buildroot}/usr/bin/sln || :
mv %{buildroot}/sbin/ldconfig %{buildroot}/usr/bin/ldconfig || :
mv %{buildroot}/usr/sbin/nscd %{buildroot}/usr/bin/nscd || :
mv %{buildroot}/usr/sbin/iconvconfig %{buildroot}/usr/bin/iconvconfig || :
#mv %{buildroot}/usr/sbin/zdump %{buildroot}/usr/bin/zdump || :
mv %{buildroot}/usr/sbin/* %{buildroot}/usr/bin/ || :

# swup compatibility hack
cp %{buildroot}/usr/lib64/libc.so.6 %{buildroot}/usr/lib64/libc-2.33.so
cp %{buildroot}/usr/lib64/libc.so.6 %{buildroot}/usr/lib64/libc-2.35.so
cp %{buildroot}/usr/lib64/ld-linux-x86-64.so.2 %{buildroot}/usr/lib64/ld-2.33.so
cp %{buildroot}/usr/lib64/ld-linux-x86-64.so.2 %{buildroot}/usr/lib64/ld-2.35.so
rm %{buildroot}/usr/lib64/libc.so.6
rm %{buildroot}/usr/lib64/ld-linux-x86-64.so.2
ln -s libc-2.35.so %{buildroot}/usr/lib64/libc.so.6
ln -s ld-2.35.so  %{buildroot}/usr/lib64/ld-linux-x86-64.so.2

rm -rf %{buildroot}/var || :
rm -rf %{buildroot}/etc || :
rm %{buildroot}/usr/share/locale/locale-archive
## install_append end
## custom find_lang start
%find_lang libc
## custom find_lang end

%files
%defattr(-,root,root,-)
