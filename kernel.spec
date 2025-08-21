# Disable building debuginfo
%global debug_package %{nil}

# Disable creation of build_id symbolic links.
%global _build_id_links none

# Disable frame pointers
%undefine _include_frame_pointers

# Disable LTO in userspace packages.
%global _lto_cflags %{nil}

# xz compress .ko
%global __spec_install_post \
  %{?__debug_package:%{__debug_install_post}} \
  %{__arch_install_post} \
  %{__os_install_post} \
  %{__mod_compress_install_post}

%global __mod_compress_install_post find %{buildroot}/lib/modules -type f -name \*.ko -print0 | xargs -0 -n 16 -r -P ${RPM_BUILD_NCPUS} xz --compress


Name: kernel
Version: 6.12.43
Release: 1%{?dist}

Summary: The Linux kernel
URL: https://www.kernel.org

License: ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-2-Clause) AND ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-3-Clause) AND ((GPL-2.0-only WITH Linux-syscall-note) OR CDDL-1.0) AND ((GPL-2.0-only WITH Linux-syscall-note) OR Linux-OpenIB) AND ((GPL-2.0-only WITH Linux-syscall-note) OR MIT) AND ((GPL-2.0-or-later WITH Linux-syscall-note) OR BSD-3-Clause) AND ((GPL-2.0-or-later WITH Linux-syscall-note) OR MIT) AND BSD-2-Clause AND (BSD-2-Clause OR Apache-2.0) AND BSD-3-Clause AND BSD-3-Clause-Clear AND CC0-1.0 AND GFDL-1.1-no-invariants-or-later AND GPL-1.0-or-later AND (GPL-1.0-or-later OR BSD-3-Clause) AND (GPL-1.0-or-later WITH Linux-syscall-note) AND GPL-2.0-only AND (GPL-2.0-only OR Apache-2.0) AND (GPL-2.0-only OR BSD-2-Clause) AND (GPL-2.0-only OR BSD-3-Clause) AND (GPL-2.0-only OR CDDL-1.0) AND (GPL-2.0-only OR GFDL-1.1-no-invariants-or-later) AND (GPL-2.0-only OR GFDL-1.2-no-invariants-only) AND (GPL-2.0-only WITH Linux-syscall-note) AND GPL-2.0-or-later AND (GPL-2.0-or-later OR BSD-2-Clause) AND (GPL-2.0-or-later OR BSD-3-Clause) AND (GPL-2.0-or-later OR CC-BY-4.0) AND (GPL-2.0-or-later WITH GCC-exception-2.0) AND (GPL-2.0-or-later WITH Linux-syscall-note) AND ISC AND LGPL-2.0-or-later AND (LGPL-2.0-or-later OR BSD-2-Clause) AND (LGPL-2.0-or-later WITH Linux-syscall-note) AND LGPL-2.1-only AND (LGPL-2.1-only OR BSD-2-Clause) AND (LGPL-2.1-only WITH Linux-syscall-note) AND LGPL-2.1-or-later AND (LGPL-2.1-or-later WITH Linux-syscall-note) AND (Linux-OpenIB OR GPL-2.0-only) AND (Linux-OpenIB OR GPL-2.0-only OR BSD-2-Clause) AND Linux-man-pages-copyleft AND MIT AND (MIT OR Apache-2.0) AND (MIT OR GPL-2.0-only) AND (MIT OR GPL-2.0-or-later) AND (MIT OR LGPL-2.1-only) AND (MPL-1.1 OR GPL-2.0-only) AND (X11 OR GPL-2.0-only) AND (X11 OR GPL-2.0-or-later) AND Zlib AND (copyleft-next-0.3.1 OR GPL-2.0-or-later)

ExclusiveArch: x86_64 aarch64 ppc64le

BuildRequires: asciidoc
BuildRequires: audit-libs-devel
BuildRequires: bash
BuildRequires: bc
BuildRequires: binutils
BuildRequires: binutils-devel
BuildRequires: bison
BuildRequires: bzip2
BuildRequires: coreutils
BuildRequires: diffutils
BuildRequires: dwarves
BuildRequires: elfutils-devel
BuildRequires: findutils
BuildRequires: flex
BuildRequires: gawk
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: git-core
BuildRequires: glibc-static
BuildRequires: gzip
BuildRequires: hmaccalc
BuildRequires: hostname
BuildRequires: java-devel
BuildRequires: kernel-rpm-macros
BuildRequires: kmod
BuildRequires: libbabeltrace-devel
BuildRequires: libbpf-devel
BuildRequires: libcap-devel
BuildRequires: libcap-ng-devel
BuildRequires: libnl3-devel
BuildRequires: libtraceevent-devel
BuildRequires: libtracefs-devel >= 1.6
BuildRequires: m4
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: net-tools
BuildRequires: newt-devel
BuildRequires: numactl-devel
BuildRequires: openssl
BuildRequires: openssl-devel
BuildRequires: pciutils-devel
BuildRequires: perl(ExtUtils::Embed)
BuildRequires: perl-Carp
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: python3-docutils
BuildRequires: python3-pyyaml
BuildRequires: python3-setuptools
BuildRequires: rsync
BuildRequires: which
BuildRequires: xmlto
BuildRequires: xz-devel
BuildRequires: zlib-devel

%ifarch aarch64
BuildRequires: opencsd-devel >= 1.2.1
%endif

Provides: installonlypkg(kernel)

Requires: %{name}-core-uname-r = %{version}-%{release}.%{_arch}
Requires: %{name}-modules-core-uname-r = %{version}-%{release}.%{_arch}
Requires: %{name}-modules-uname-r = %{version}-%{release}.%{_arch}

Source: linux-%(echo %{version} | awk -F. '{print $1"."$2}').tar.xz

%if 0%(echo %{version} | awk -F. '{print $3}')
Patch: patch-%{version}.xz
%endif


Source091: kernel-el9-x86_64.config
Source092: kernel-el9-aarch64.config
Source093: kernel-el9-ppc64le.config


Patch: 0001-ACPI-APEI-arm64-Ignore-broken-HPE-moonshot-APEI-support.patch
Patch: 0002-ACPI-irq-Workaround-firmware-issue-on-X-Gene-based-m400.patch
Patch: 0003-aarch64-acpi-scan-Fix-regression-related-to-X-Gene-UARTs.patch
Patch: 0004-Vulcan-AHCI-PCI-bar-fix-for-Broadcom-Vulcan-early-silicon.patch
Patch: 0005-ahci-thunderx2-Fix-for-errata-that-affects-stop-engine.patch
Patch: 0006-ipmi-do-not-configure-ipmi-for-HPE-m400.patch
Patch: 0007-iommu-arm-smmu-workaround-DMA-mode-issues.patch
Patch: 0008-Add-efi_status_to_str-and-rework-efi_status_to_err.patch
Patch: 0009-Make-get_cert_list-use-efi_status_to_str-to-print-error-messages.patch
Patch: 0010-security-lockdown-expose-a-hook-to-lock-the-kernel-down.patch
Patch: 0011-efi-Add-an-EFI_SECURE_BOOT-flag-to-indicate-secure-boot-mode.patch
Patch: 0012-efi-Lock-down-the-kernel-if-booted-in-secure-boot-mode.patch
Patch: 0013-ARM-tegra-usb-no-reset.patch
Patch: 0014-Input-rmi4-remove-the-need-for-artificial-IRQ-in-case-of-HID.patch
Patch: 0015-KEYS-Make-use-of-platform-keyring-for-module-signature-verify.patch
Patch: 0016-REDHAT-coresight-etm4x-Disable-coresight-on-HPE-Apollo-70.patch
Patch: 0017-Change-acpi_bus_get_acpi_device-to-acpi_get_acpi_dev.patch
Patch: 0018-scsi-sd-Add-probe_type-module-parameter-to-allow-synchronous-probing.patch
Patch: 0019-lsm-update-security_lock_kernel_down.patch


%description
The kernel meta package.


%package core
Summary: The linux kernel
AutoReq: no
AutoProv: yes

Provides: installonlypkg(kernel)
Provides: %{name} = %{version}-%{release}
Provides: %{name}-core-uname-r = %{version}-%{release}.%{_arch}
Provides: %{name}-uname-r = %{version}-%{release}.%{_arch}

Requires: %{name}-modules-core-uname-r = %{version}-%{release}.%{_arch}

Requires(preun): %{_bindir}/kernel-install
Requires(post): coreutils
Requires(posttrans): %{_bindir}/kernel-install

Recommends: linux-firmware

%description core
The %{name} package contains the Linux kernel (vmlinuz), the core of any
Linux operating system. The kernel handles the basic functions
of the operating system: memory allocation, process allocation, device
input and output, etc.


%package modules
Summary: kernel modules to match the %{name}
AutoReq: no
AutoProv: yes

Provides: installonlypkg(kernel-module)
Provides: %{name}-modules-uname-r = %{version}-%{release}.%{_arch}
Provides: %{name}-modules-core = %{version}-%{release}
Provides: %{name}-modules-core-uname-r = %{version}-%{release}.%{_arch}
Provides: %{name}-modules-extra = %{version}-%{release}
Provides: %{name}-modules-extra-uname-r = %{version}-%{release}.%{_arch}

Requires: %{name}-uname-r = %{version}-%{release}.%{_arch}

Requires(post): coreutils

%description modules
This package provides kernel modules for the %{name} package.


%package devel
Summary: Development package for building kernel modules to match the %{name}
AutoReq: no
AutoProv: no

Provides: installonlypkg(kernel)
Provides: %{name}-devel-uname-r = %{version}-%{release}.%{_arch}

Requires: bison
Requires: elfutils-libelf-devel
Requires: findutils
Requires: flex
Requires: gcc
Requires: make
Requires: openssl-devel
Requires: perl-interpreter

%description devel
This package provides kernel headers and makefiles sufficient to build modules
against the %{name} package.


%package devel-matched
Summary: Meta package to install matching core and devel packages for a given %{name}
Requires: %{name}-devel = %{version}-%{release}
Requires: %{name}-core = %{version}-%{release}

%description devel-matched
This meta package is used to install matching core and devel packages for a given %{name}.


%package headers
Summary: Header files for the Linux kernel for use by glibc
Obsoletes: glibc-kernheaders < 3.0-46
Provides: glibc-kernheaders = 3.0-46

%description headers
Kernel-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
glibc package.


%package cross-headers
Summary: Header files for the Linux kernel for use by cross-glibc

%description cross-headers
Kernel-cross-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
cross-glibc package.


%package -n perf
Summary: Performance monitoring for the Linux kernel
Requires: bzip2

%description -n perf
This package contains the perf tool, which enables performance monitoring
of the Linux kernel.


%package -n python3-perf
Summary: Python bindings for apps which will manipulate perf events

%description -n python3-perf
The python3-perf package contains a module that permits applications
written in the Python programming language to use the interface
to manipulate perf events.


%package -n libperf
Summary: The perf library from kernel source

%description -n libperf
This package contains the kernel source perf library.


%package -n libperf-devel
Summary: Developement files for the perf library from kernel source
Requires: libperf = %{version}-%{release}

%description -n libperf-devel
This package includes libraries and header files needed for development
of applications which use perf library from kernel source.


%package tools
Summary: Assortment of tools for the Linux kernel
Provides: cpupowerutils = 1:009-0.6.p1
Provides: cpufreq-utils = 1:009-0.6.p1
Provides: cpufrequtils = 1:009-0.6.p1
Obsoletes: cpupowerutils < 1:009-0.6.p1
Obsoletes: cpufreq-utils < 1:009-0.6.p1
Obsoletes: cpufrequtils < 1:009-0.6.p1
Obsoletes: cpuspeed < 1:1.5-16
Requires: %{name}-tools-libs = %{version}-%{release}

%define __requires_exclude ^%{_bindir}/python

%description tools
This package contains the tools/ directory from the kernel source
and the supporting documentation.


%package tools-libs
Summary: Libraries for the kernels-tools

%description tools-libs
This package contains the libraries built from the tools/ directory
from the kernel source.


%package tools-libs-devel
Summary: Assortment of tools for the Linux kernel

Provides: %{name}-tools-devel
Provides: cpupowerutils-devel = 1:009-0.6.p1
Obsoletes: cpupowerutils-devel < 1:009-0.6.p1
Requires: %{name}-tools = %{version}-%{release}
Requires: %{name}-tools-libs = %{version}-%{release}

%description tools-libs-devel
This package contains the development files for the tools/ directory from
the kernel source.


%package -n rtla
Summary: Real-Time Linux Analysis tools

%description -n rtla
The rtla meta-tool includes a set of commands that aims to analyze
the real-time properties of Linux. Instead of testing Linux as a black box,
rtla leverages kernel tracing capabilities to provide precise information
about the properties and root causes of unexpected results.


%package -n rv
Summary: RV: Runtime Verification

%description -n rv
Runtime Verification (RV) is a lightweight (yet rigorous) method that
complements classical exhaustive verification techniques (such as model
checking and theorem proving) with a more practical approach for
complex systems.
The rv tool is the interface for a collection of monitors that aim
analysing the logical and timing behavior of Linux.


%ifarch x86_64
%define asmarch x86
%define hdrarch x86_64
%endif

%ifarch aarch64
%define asmarch arm64
%define hdrarch arm64
%endif

%ifarch ppc64le
%define asmarch powerpc
%define hdrarch powerpc
%endif

%global make %{__make} %{_make_output_sync} %{?_smp_mflags}
%global make_kernel %{make} ARCH=%{hdrarch} HOSTCFLAGS="%{?build_cflags}" HOSTLDFLAGS="%{?build_ldflags}"

%global make_tools CFLAGS="%{?build_cflags}" LDFLAGS="%{?build_ldflags}" EXTRA_CFLAGS="%{?build_cflags}" %{make_kernel}

%ifarch aarch64
%global make_perf_extra_opts CORESIGHT=1
%endif
%global make_perf %{make} EXTRA_CFLAGS="%{?build_cflags}" EXTRA_CXXFLAGS="%{?build_cxxflags}" LDFLAGS="%{?build_ldflags} -Wl,-E" -C tools/perf NO_PERF_READ_VDSO32=1 NO_PERF_READ_VDSOX32=1 WERROR=0 NO_LIBUNWIND=1 HAVE_CPLUS_DEMANGLE=1 NO_GTK2=1 NO_STRLCPY=1 NO_BIONIC=1 LIBBPF_DYNAMIC=1 LIBTRACEEVENT_DYNAMIC=1 %{?make_perf_extra_opts} prefix=%{_prefix} PYTHON=%{__python3}

%global make_libperf %{make} EXTRA_CFLAGS="%{?build_cflags}" LDFLAGS="%{?build_ldflags}" -C tools/lib/perf


%prep
%autosetup -p1 -n linux-%(echo %{version} | awk -F. '{print $1"."$2}')

echo "Fixing Python shebangs..."
%py3_shebang_fix \
	tools/kvm/kvm_stat/kvm_stat \
	scripts/show_delta \
	scripts/diffconfig \
	scripts/bloat-o-meter \
	scripts/jobserver-exec \
	tools \
	Documentation \
	scripts/clang-tools

# Delete .gitingore files from sources
find . -name .gitignore -delete

sed -i "s@^EXTRAVERSION.*@EXTRAVERSION = -%{release}.%{_arch}@" Makefile

mv COPYING COPYING-%{version}-%{release}

cp %{_sourcedir}/kernel-el%{rhel}-%{_arch}.config .config

echo "New config options..."
%{make_kernel} listnewconfig
%{make_kernel} olddefconfig


%build
%ifarch x86_64
%{make_kernel} bzImage
%endif

%ifarch aarch64
%{make_kernel} vmlinuz.efi
%endif

%ifarch ppc64le
%{make_kernel} vmlinux
%endif

%{make_kernel} modules || exit 1

%ifarch aarch64
%{make_kernel} dtbs
%endif

%{__chmod} +x tools/perf/check-headers.sh
%{make_perf} DESTDIR=%{buildroot} all
%{make_libperf} DESTDIR=%{buildroot}

%{__chmod} +x tools/power/cpupower/utils/version-gen.sh
%{make_tools} -C tools/power/cpupower CPUFREQ_BENCH=false DEBUG=false

%ifarch x86_64
pushd tools/power/cpupower/debug/x86_64
%{make_tools} centrino-decode powernow-k8-decode
popd
pushd tools/power/x86/x86_energy_perf_policy/
%{make_tools}
popd
pushd tools/power/x86/turbostat
%{make_tools}
popd
pushd tools/power/x86/intel-speed-select
%{make_tools}
popd
pushd tools/arch/x86/intel_sdsi
%{make_tools} CFLAGS="%{?build_cflags}"
popd
%endif

pushd tools/thermal/tmon/
%{make_tools}
popd
pushd tools/iio/
%{make_tools}
popd
pushd tools/gpio/
%{make_tools}
popd
pushd tools/mm/
%{make_tools} slabinfo page_owner_sort
popd
pushd tools/verification/rv/
%{make_tools}
popd
pushd tools/tracing/rtla
%{make_tools}
popd

# Build the bootstrap bpftool to generate vmlinux.h
export BPFBOOTSTRAP_CFLAGS=$(echo "%{__global_compiler_flags}" | sed -r "s/\-specs=[^\ ]+\/redhat-annobin-cc1//")
export BPFBOOTSTRAP_LDFLAGS=$(echo "%{build_ldflags}" | sed -r "s/\-specs=[^\ ]+\/redhat-annobin-cc1//")
CFLAGS="" LDFLAGS="" %{make} EXTRA_CFLAGS="${BPFBOOTSTRAP_CFLAGS}" EXTRA_CXXFLAGS="${BPFBOOTSTRAP_CFLAGS}" EXTRA_LDFLAGS="${BPFBOOTSTRAP_LDFLAGS}" -C tools/bpf/bpftool bootstrap
tools/bpf/bpftool/bootstrap/bpftool btf dump file vmlinux format c > vmlinux.h


%install
%{__install} -d %{buildroot}/boot
%{__install} -d %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}
%{__install} -d %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/systemtap

%{__install} -m 644 .config %{buildroot}/boot/config-%{version}-%{release}.%{_arch}
%{__install} -m 644 .config %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/config
%{__install} -m 644 System.map %{buildroot}/boot/System.map-%{version}-%{release}.%{_arch}
%{__install} -m 644 System.map %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/System.map

%ifarch x86_64
%{__install} -m 755 arch/%{asmarch}/boot/bzImage %{buildroot}/boot/vmlinuz-%{version}-%{release}.%{_arch}
%endif

%ifarch aarch64
%{__install} -m 755 arch/%{asmarch}/boot/vmlinuz.efi %{buildroot}/boot/vmlinuz-%{version}-%{release}.%{_arch}
%endif

%ifarch ppc64le
%{__install} -m 755 vmlinux %{buildroot}/boot/vmlinuz-%{version}-%{release}.%{_arch}
%endif

cp %{buildroot}/boot/vmlinuz-%{version}-%{release}.%{_arch} %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/vmlinuz

(cd %{buildroot}/boot && sha512hmac vmlinuz-%{version}-%{release}.%{_arch}) > %{buildroot}/boot/.vmlinuz-%{version}-%{release}.%{_arch}.hmac
cp %{buildroot}/boot/.vmlinuz-%{version}-%{release}.%{_arch}.hmac %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/.vmlinuz.hmac

%{make_kernel} INSTALL_MOD_PATH=%{buildroot} modules_install KERNELRELEASE=%{version}-%{release}.%{_arch} mod-fw=

%ifnarch ppc64le
%{make_kernel} INSTALL_MOD_PATH=%{buildroot} vdso_install KERNELRELEASE=%{version}-%{release}.%{_arch}
rm -rf %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/vdso/.build-id
%endif

%ifarch aarch64
%{make_kernel} dtbs_install INSTALL_DTBS_PATH=%{buildroot}/boot/dtb-%{version}-%{release}.%{_arch}
cp -r %{buildroot}/boot/dtb-%{version}-%{release}.%{_arch} %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/dtb
find arch/%{asmarch}/boot/dts -name '*.dtb' -type f -delete
%endif

rm -f %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/{build,source}
%{__install} -d %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
%{__install} -d %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/extra
%{__install} -d %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/updates
%{__install} -d %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/weak-updates
ln -s build %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/source

# First copy everything
cp --parents `find  -type f -name "Makefile*" -o -name "Kconfig*"` %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build

%{__install} -m 644 -D -t %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build Module.symvers
%{__install} -m 644 -D -t %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build System.map
%{__install} -m 644 -D -t %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build vmlinux.h

gzip -c9 < Module.symvers > %{buildroot}/boot/symvers-%{version}-%{release}.%{_arch}.gz
cp %{buildroot}/boot/symvers-%{version}-%{release}.%{_arch}.gz %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/symvers.gz

# then delete all files but the needed Makefiles and config files.
rm -rf %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build/{include,scripts}
%{__install} -m 644 -D -t %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build .config
cp -a scripts %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
rm -rf %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build/scripts/tracing
rm -f %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build/scripts/spdxcheck.py

# Files for 'make scripts' to succeed with kernel-devel.
%{__install} -d %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build/security/selinux/include
cp -a --parents security/selinux/include/classmap.h %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents security/selinux/include/initial_sid_to_string.h %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
%{__install} -d  %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build/tools/include/tools
cp -a --parents tools/include/tools/be_byteshift.h %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents tools/include/tools/le_byteshift.h %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build

# Files for 'make prepare' to succeed with kernel-devel.
cp -a --parents tools/include/linux/compiler* %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents tools/include/linux/types.h %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents tools/build/Build.include %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp --parents tools/build/fixdep.c %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp --parents tools/objtool/sync-check.sh %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents tools/bpf/resolve_btfids %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build

cp --parents security/selinux/include/policycap_names.h %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp --parents security/selinux/include/policycap.h %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build

cp -a --parents tools/include/asm %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents tools/include/asm-generic %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents tools/include/linux %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents tools/include/uapi/asm %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents tools/include/uapi/asm-generic %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents tools/include/uapi/linux %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents tools/include/vdso %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp --parents tools/scripts/utilities.mak %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents tools/lib/subcmd %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp --parents tools/lib/*.c %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp --parents tools/objtool/*.[ch] %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp --parents tools/objtool/Build %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp --parents tools/objtool/include/objtool/*.h %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents tools/lib/bpf %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp --parents tools/lib/bpf/Build %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build

%ifarch x86_64
cp -a --parents tools/objtool/objtool %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents tools/objtool/fixdep %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
%endif

cp -a --parents include %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents arch/%{asmarch}/include %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents sound/soc/sof/sof-audio.h %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build/sound/soc/sof
cp -a --parents tools/arch/%{asmarch}/include %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build

%ifarch ppc64le
cp -a --parents arch/%{asmarch}/lib/crtsavres.[So] %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
%endif

%ifarch aarch64
cp -a --parents arch/arm/include/asm/xen %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents arch/arm/include/asm/opcodes.h %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
%endif

%ifarch x86_64
# files for 'make prepare' to succeed with kernel-devel
cp -a --parents arch/x86/entry/syscalls/syscall_32.tbl %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents arch/x86/entry/syscalls/syscall_64.tbl %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents arch/x86/tools/relocs_32.c %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents arch/x86/tools/relocs_64.c %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents arch/x86/tools/relocs.c %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents arch/x86/tools/relocs_common.c %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents arch/x86/tools/relocs.h %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents arch/x86/purgatory/purgatory.c %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents arch/x86/purgatory/stack.S %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents arch/x86/purgatory/setup-x86_64.S %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents arch/x86/purgatory/entry64.S %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents arch/x86/boot/string.h %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents arch/x86/boot/string.c %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents arch/x86/boot/ctype.h %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build

cp -a --parents scripts/syscalltbl.sh %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents scripts/syscallhdr.sh %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build

cp -a --parents tools/arch/x86/include/asm %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents tools/arch/x86/include/uapi/asm %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents tools/objtool/arch/x86/lib %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents tools/arch/x86/lib/ %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents tools/arch/x86/tools/gen-insn-attr-x86.awk %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
cp -a --parents tools/objtool/arch/x86/ %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build
%endif

# Clean up intermediate files
find %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build/scripts \( -iname "*.o" -o -iname "*.cmd" \) -delete
find %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build/tools \( -iname "*.o" -o -iname "*.cmd" \) -delete

# Make sure the Makefile, version.h, and auto.conf have a matching timestamp so that external modules can be built
touch -r %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build/Makefile \
    %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build/include/generated/uapi/linux/version.h \
    %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build/include/config/auto.conf

# Remove files to be auto generated by depmod
pushd %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}
rm -f modules.{alias,alias.bin,builtin.alias.bin,builtin.bin,dep,dep.bin,devname,softdep,symbols,symbols.bin,weakdep}
popd

%{__install} -d %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/kernel
touch %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/modules.order
touch %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/modules.builtin

# Move the devel headers out of the root file system
%{__install} -d %{buildroot}/%{_usrsrc}/kernels
mv %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build %{buildroot}/%{_usrsrc}/kernels/%{version}-%{release}.%{_arch}
ln -sf %{_usrsrc}/kernels/%{version}-%{release}.%{_arch} %{buildroot}/lib/modules/%{version}-%{release}.%{_arch}/build

# Prune unwanted files
find %{buildroot}/%{_usrsrc}/kernels \( -iname "*.mod.c" -o -iname "*.cmd" \) -delete

# Remove debuginfo
rm -rf %{buildroot}/%{_prefix}/lib/debug

# Estimate the size of the initramfs (See BZ #530778)
dd if=/dev/zero of=%{buildroot}/boot/initramfs-%{version}-%{release}.%{_arch}.img bs=1M count=20

# Make .ko objects temporarily executable for automatic stripping
find %{buildroot}/lib/modules -type f -name \*.ko -exec %{__chmod} u+x \{\} \+

# Blacklist selected modules
%{__install} -d %{buildroot}/%{_sysconfdir}/modprobe.d
for mod in floppy
do
    echo "blacklist $mod" > %{buildroot}/%{_sysconfdir}/modprobe.d/$mod.conf
done

# kernel-headers
%{make} ARCH=%{hdrarch} INSTALL_HDR_PATH=%{buildroot}/%{_prefix} headers_install
find %{buildroot}/%{_includedir} \( -name .install -o -name .check -o -name ..install.cmd -o -name ..check.cmd \) -delete

# kernel-cross-headers
ASMARCHS=(arm64 powerpc x86)
HDRARCHS=(arm64 powerpc x86_64)

for p in "${!ASMARCHS[@]}"
do
    %{make} ARCH=${HDRARCHS[p]} INSTALL_HDR_PATH=%{buildroot}/%{_prefix}/${ASMARCHS[p]}-linux-gnu headers_install
    find %{buildroot}/%{_prefix}/${ASMARCHS[p]}-linux-gnu \( -name .install -o -name .check -o -name ..install.cmd -o -name ..check.cmd \) -delete
done

# perf
%{make_perf} DESTDIR=%{buildroot} lib=%{_lib} install-bin
%{__install} -m 644 -D -t %{buildroot}/%{_docdir}/perf tools/perf/Documentation/examples.txt

# Remove unwanted files
rm -f %{buildroot}%{_bindir}/trace
rm -rf %{buildroot}/%{_prefix}/lib/perf/examples
rm -rf %{buildroot}/%{_prefix}/lib/perf/include

# python-perf extension
%{make_perf} DESTDIR=%{buildroot} install-python_ext

# perf man pages
%{__install} -d %{buildroot}/%{_mandir}/man1
%{make_perf} DESTDIR=%{buildroot} install-man

# Remove unwanted files
rm -rf %{buildroot}%{_libdir}/traceevent

# libperf
%{make_libperf} -j 1 DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{_libdir} install install_headers

# tools
%{make_tools} -C tools/power/cpupower DESTDIR=%{buildroot} libdir=%{_libdir} mandir=%{_mandir} CPUFREQ_BENCH=false install
%find_lang cpupower
%ifarch x86_64
pushd tools/power/cpupower/debug/x86_64
%{__install} -m 755 centrino-decode %{buildroot}%{_bindir}/centrino-decode
%{__install} -m 755 powernow-k8-decode %{buildroot}%{_bindir}/powernow-k8-decode
popd
%endif
%{__chmod} 0755 %{buildroot}%{_libdir}/libcpupower.so*

%ifarch x86_64
%{__install} -d %{buildroot}%{_mandir}/man8
pushd tools/power/x86/x86_energy_perf_policy
%{make_tools} DESTDIR=%{buildroot} install
popd
pushd tools/power/x86/turbostat
%{make_tools} DESTDIR=%{buildroot} install
popd
pushd tools/power/x86/intel-speed-select
%{make_tools} DESTDIR=%{buildroot} install
popd
pushd tools/arch/x86/intel_sdsi
%{make_tools} CFLAGS="%{?build_cflags}" DESTDIR=%{buildroot} install
popd
%endif

pushd tools/thermal/tmon
%{make_tools} INSTALL_ROOT=%{buildroot} install
popd
pushd tools/bootconfig
%{make_tools} DESTDIR=%{buildroot} install
popd
pushd tools/iio
%{make_tools} DESTDIR=%{buildroot} install
popd
pushd tools/gpio
%{make_tools} DESTDIR=%{buildroot} install
popd

pushd tools/kvm/kvm_stat
%{make} INSTALL_ROOT=%{buildroot} install-tools
%{make} INSTALL_ROOT=%{buildroot} install-man
%{__install} -m 644 -D -t %{buildroot}%{_unitdir} kvm_stat.service
%{__install} -d %{buildroot}%{_sysconfdir}/logrotate.d
cat > %{buildroot}%{_sysconfdir}/logrotate.d/kvm_stat << EOF
/var/log/kvm_stat.csv {
	size 10M
	missingok
	compress
	maxage 30
	rotate 5
	nodateext
	postrotate
		/usr/bin/systemctl try-restart kvm_stat.service
	endscript
}
EOF
popd

pushd tools/mm/
%{__install} -m 755 -D -t %{buildroot}%{_bindir} slabinfo
%{__install} -m 755 -D -t %{buildroot}%{_bindir} page_owner_sort
popd
pushd tools/verification/rv/
%{make_tools} DESTDIR=%{buildroot} install
popd
pushd tools/tracing/rtla/
%{make_tools} DESTDIR=%{buildroot} install
rm -f %{buildroot}%{_bindir}/hwnoise
rm -f %{buildroot}%{_bindir}/osnoise
rm -f %{buildroot}%{_bindir}/timerlat
ln -sf rtla %{buildroot}/%{_bindir}/hwnoise
ln -sf rtla %{buildroot}/%{_bindir}/osnoise
ln -sf rtla %{buildroot}/%{_bindir}/timerlat
popd

# Remove static libraries
rm -rf %{buildroot}%{_libdir}/*.{a,la}


%post core
mkdir -p %{_localstatedir}/lib/rpm-state/%{name}
touch %{_localstatedir}/lib/rpm-state/%{name}/core-%{version}-%{release}.%{_arch}
rm -f %{_localstatedir}/lib/rpm-state/%{name}/modules-%{version}-%{release}.%{_arch}

%preun core
kernel-install remove %{version}-%{release}.%{_arch} || exit $?
if [ -x %{_sbindir}/weak-modules ]
then
    %{_sbindir}/weak-modules --remove-kernel %{version}-%{release}.%{_arch} || exit $?
fi

%posttrans core
if [ -f %{_localstatedir}/lib/rpm-state/%{name}/core-%{version}-%{release}.%{_arch} ]
then
    rm -f %{_localstatedir}/lib/rpm-state/%{name}/core-%{version}-%{release}.%{_arch}
    kernel-install add %{version}-%{release}.%{_arch} /lib/modules/%{version}-%{release}.%{_arch}/vmlinuz || exit $?
    if [ -x %{_sbindir}/weak-modules ]
    then
        %{_sbindir}/weak-modules --add-kernel %{version}-%{release}.%{_arch} || exit $?
    fi
fi


%files


%files core
%license COPYING-%{version}-%{release}
%ghost %attr(0644, root, root) /boot/config-%{version}-%{release}.%{_arch}
%ghost %attr(0600, root, root) /boot/initramfs-%{version}-%{release}.%{_arch}.img
%ghost %attr(0644, root, root) /boot/symvers-%{version}-%{release}.%{_arch}.gz
%ghost /boot/System.map-%{version}-%{release}.%{_arch}
%ghost /boot/vmlinuz-%{version}-%{release}.%{_arch}
%ghost /boot/.vmlinuz-%{version}-%{release}.%{_arch}.hmac
/lib/modules/%{version}-%{release}.%{_arch}/config
/lib/modules/%{version}-%{release}.%{_arch}/modules.builtin*
/lib/modules/%{version}-%{release}.%{_arch}/symvers.gz
/lib/modules/%{version}-%{release}.%{_arch}/System.map
/lib/modules/%{version}-%{release}.%{_arch}/vmlinuz
/lib/modules/%{version}-%{release}.%{_arch}/.vmlinuz.hmac

%ifarch aarch64
%ghost /boot/dtb-%{version}-%{release}.%{_arch}
/lib/modules/%{version}-%{release}.%{_arch}/dtb
%endif


%files modules
%config(noreplace) /etc/modprobe.d/*.conf
%dir /lib/modules
%dir /lib/modules/%{version}-%{release}.%{_arch}
%ghost %attr(0644, root, root) /lib/modules/%{version}-%{release}.%{_arch}/modules.alias
%ghost %attr(0644, root, root) /lib/modules/%{version}-%{release}.%{_arch}/modules.alias.bin
%ghost %attr(0644, root, root) /lib/modules/%{version}-%{release}.%{_arch}/modules.builtin.alias.bin
%ghost %attr(0644, root, root) /lib/modules/%{version}-%{release}.%{_arch}/modules.builtin.bin
%ghost %attr(0644, root, root) /lib/modules/%{version}-%{release}.%{_arch}/modules.dep
%ghost %attr(0644, root, root) /lib/modules/%{version}-%{release}.%{_arch}/modules.dep.bin
%ghost %attr(0644, root, root) /lib/modules/%{version}-%{release}.%{_arch}/modules.devname
%ghost %attr(0644, root, root) /lib/modules/%{version}-%{release}.%{_arch}/modules.softdep
%ghost %attr(0644, root, root) /lib/modules/%{version}-%{release}.%{_arch}/modules.symbols
%ghost %attr(0644, root, root) /lib/modules/%{version}-%{release}.%{_arch}/modules.symbols.bin
%ghost %attr(0644, root, root) /lib/modules/%{version}-%{release}.%{_arch}/modules.weakdep
/lib/modules/%{version}-%{release}.%{_arch}/build
/lib/modules/%{version}-%{release}.%{_arch}/source
/lib/modules/%{version}-%{release}.%{_arch}/systemtap
/lib/modules/%{version}-%{release}.%{_arch}/extra
/lib/modules/%{version}-%{release}.%{_arch}/updates
/lib/modules/%{version}-%{release}.%{_arch}/weak-updates
/lib/modules/%{version}-%{release}.%{_arch}/modules.order
%ifnarch ppc64le
/lib/modules/%{version}-%{release}.%{_arch}/vdso
%endif
%defattr(644,root,root,755)
/lib/modules/%{version}-%{release}.%{_arch}/kernel


%files devel
%defverify(not mtime)
%{_usrsrc}/kernels/%{version}-%{release}.%{_arch}


%files devel-matched


%files headers
%{_includedir}/*
%exclude %{_includedir}/cpufreq.h


%files cross-headers
%{_prefix}/*-linux-gnu/include/*


%files -n perf
%{_bindir}/perf
%{_datadir}/perf-core
%{_docdir}/perf*
%{_includedir}/perf/perf_dlfilter.h
%{_libdir}/libperf-jvmti.so
%{_libexecdir}/perf-core
%{_mandir}/man*/perf*
%{_sysconfdir}/bash_completion.d/perf


%files -n python3-perf
%{python3_sitearch}/*


%files -n libperf
%{_libdir}/libperf.so.0
%{_libdir}/libperf.so.0.0.1


%files -n libperf-devel
%{_docdir}/libperf
%{_includedir}/internal/*.h
%{_includedir}/perf/bpf_perf.h
%{_includedir}/perf/core.h
%{_includedir}/perf/cpumap.h
%{_includedir}/perf/event.h
%{_includedir}/perf/evlist.h
%{_includedir}/perf/evsel.h
%{_includedir}/perf/mmap.h
%{_includedir}/perf/threadmap.h
%{_libdir}/libperf.so
%{_libdir}/pkgconfig/libperf.pc
%{_mandir}/man*/libperf*


%files tools -f cpupower.lang
%config(noreplace) %{_sysconfdir}/logrotate.d/kvm_stat
%{_bindir}/bootconfig
%{_bindir}/cpupower
%{_bindir}/gpio-event-mon
%{_bindir}/gpio-hammer
%{_bindir}/gpio-watch
%{_bindir}/iio_event_monitor
%{_bindir}/iio_generic_buffer
%{_bindir}/kvm_stat
%{_bindir}/lsgpio
%{_bindir}/lsiio
%{_bindir}/page_owner_sort
%{_bindir}/slabinfo
%{_bindir}/tmon
%{_datadir}/bash-completion/completions/cpupower
%{_mandir}/man*/cpupower*
%{_mandir}/man*/kvm_stat*
%{_unitdir}/kvm_stat.service

%ifarch x86_64
%{_bindir}/centrino-decode
%{_bindir}/intel-speed-select
%{_bindir}/powernow-k8-decode
%{_bindir}/turbostat
%{_bindir}/x86_energy_perf_policy
%{_mandir}/man*/turbostat*
%{_mandir}/man*/x86_energy_perf_policy*
%{_sbindir}/intel_sdsi
%endif


%files tools-libs
%{_libdir}/libcpupower.so.1
%{_libdir}/libcpupower.so.0.0.1


%files tools-libs-devel
%{_includedir}/cpufreq.h
%{_includedir}/cpuidle.h
%{_includedir}/powercap.h
%{_libdir}/libcpupower.so


%files -n rtla
%{_bindir}/hwnoise
%{_bindir}/osnoise
%{_bindir}/rtla
%{_bindir}/timerlat
%{_mandir}/man*/rtla*

%files -n rv
%{_bindir}/rv
%{_mandir}/man*/rv*


%changelog
* Thu Aug 21 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.43-1
- Update to 6.12.43

* Sat Aug 16 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.42-1
- Update to 6.12.42

* Sat Aug 02 2025 Peter Georg <peter.georg@physik.uni-regensburg.de> - 6.12.41-2
- Turn off support for Rust

* Fri Aug 01 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.41-1
- Update to 6.12.41

* Thu Jul 24 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.40-1
- Update to 6.12.40

* Fri Jul 18 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.39-1
- Update to 6.12.39

* Mon Jul 14 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.38-1
- Update to 6.12.38

* Fri Jul 11 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.37-1
- Update to 6.12.37

* Mon Jul 07 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.36-1
- Update to 6.12.36

* Fri Jun 27 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.35-1
- Update to 6.12.35

* Fri Jun 20 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.34-1
- Update to 6.12.34

* Wed Jun 11 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.33-1
- Update to 6.12.33

* Thu Jun 05 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.32-1
- Update to 6.12.32

* Fri May 30 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.31-1
- Update to 6.12.31

* Fri May 23 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.30-1
- Update to 6.12.30

* Sun May 18 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.29-1
- Update to 6.12.29

* Sat May 10 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.28-1
- Update to 6.12.28

* Mon May 05 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.27-1
- Update to 6.12.27

* Fri May 02 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.26-1
- Update to 6.12.26

* Fri Apr 25 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.25-1
- Update to 6.12.25

* Mon Apr 21 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.24-1
- Update to 6.12.24

* Fri Apr 11 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.23-1
- Update to 6.12.23

* Tue Apr 08 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.22-1
- Update to 6.12.22

* Sat Mar 29 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.21-1
- Update to 6.12.21

* Sun Mar 23 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.20-1
- Update to 6.12.20

* Thu Mar 13 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.19-1
- Update to 6.12.19

* Fri Mar 07 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.18-1
- Update to 6.12.18

* Thu Feb 27 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.17-1
- Update to 6.12.17

* Fri Feb 21 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.16-1
- Update to 6.12.16

* Tue Feb 18 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.15-1
- Update to 6.12.15

* Tue Feb 18 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.14-1
- Update to 6.12.14

* Sat Feb 08 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.13-1
- Update to 6.12.13

* Sun Feb 02 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.12-1
- Update to 6.12.12

* Fri Jan 24 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.11-1
- Update to 6.12.11

* Sat Jan 18 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.10-1
- Update to 6.12.10

* Thu Jan 09 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.9-1
- Update to 6.12.9

* Fri Jan 03 2025 Kmods SIG <sig-kmods@centosproject.org> - 6.12.8-1
- Update to 6.12.8

* Sat Dec 28 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.12.7-1
- Update to 6.12.7

* Fri Dec 20 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.12.6-1
- Update to 6.12.6

* Sun Dec 15 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.12.5-1
- Update to 6.12.5

* Mon Dec 09 2024 Peter Georg <peter.georg@physik.uni-regensburg.de> - 6.12.4-1
- Update to 6.12.4

* Thu Dec 05 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.11.11-1
- Update to 6.11.11

* Fri Nov 22 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.11.10-1
- Update to 6.11.10

* Fri Nov 22 2024 Peter Georg <peter.georg@physik.uni-regensburg.de> - 6.11.9-2
- Turn on support for Rust

* Mon Nov 18 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.11.9-1
- Update to 6.11.9

* Fri Nov 15 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.11.8-1
- Update to 6.11.8

* Wed Nov 13 2024 Peter Georg <peter.georg@physik.uni-regensburg.de> - 6.11.7-2
- Re-enable CORESIGHT=1 on aarch64
- Re-enable building tool rtla

* Sat Nov 09 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.11.7-1
- Update to 6.11.7

* Fri Nov 01 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.11.6-1
- Update to 6.11.6

* Tue Oct 22 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.11.5-1
- Update to 6.11.5

* Thu Oct 17 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.11.4-1
- Update to 6.11.4

* Fri Oct 11 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.11.3-1
- Update to 6.11.3

* Fri Oct 04 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.11.2-1
- Update to 6.11.2

* Thu Oct 03 2024 Peter Georg <peter.georg@physik.uni-regensburg.de> - 6.11.1-1
- Update to 6.11.1

* Tue Oct 01 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.10.12-1
- Update to 6.10.12

* Thu Sep 19 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.10.11-1
- Update to 6.10.11

* Fri Sep 13 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.10.10-1
- Update to 6.10.10

* Sun Sep 08 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.10.9-1
- Update to 6.10.9

* Fri Sep 06 2024 Peter Georg <peter.georg@physik.uni-regensburg.de> - 6.10.8-2
- Use bootstrapped bpftool to build vmlinux.h

* Wed Sep 04 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.10.8-1
- Update to 6.10.8

* Fri Aug 30 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.10.7-1
- Update to 6.10.7

* Mon Aug 19 2024 Peter Georg <peter.georg@physik.uni-regensburg.de> - 6.10.6-2
- Enable OCP TimeCard and dependencies

* Mon Aug 19 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.10.6-1
- Update to 6.10.6

* Wed Aug 14 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.10.5-1
- Update to 6.10.5

* Sun Aug 11 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.10.4-1
- Update to 6.10.4

* Sat Aug 03 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.10.3-1
- Update to 6.10.3

* Mon Jul 29 2024 Peter Georg <peter.georg@physik.uni-regensburg.de> - 6.10.2-1
- Update to 6.10.2
- Disable building tool rtla (Requires libtracefs 1.6)

* Sun Jul 28 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.9.12-1
- Update to 6.9.12

* Thu Jul 25 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.9.11-1
- Update to 6.9.11

* Thu Jul 18 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.9.10-1
- Update to 6.9.10

* Thu Jul 11 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.9.9-1
- Update to 6.9.9

* Fri Jul 05 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.9.8-1
- Update to 6.9.8

* Thu Jun 27 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.9.7-1
- Update to 6.9.7

* Fri Jun 21 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.9.6-1
- Update to 6.9.6

* Sun Jun 16 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.9.5-1
- Update to 6.9.5

* Wed Jun 12 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.9.4-1
- Update to 6.9.4

* Wed Jun 12 2024 Peter Georg <peter.georg@physik.uni-regensburg.de> - 6.9.3-1
- Update to 6.9.3

* Fri May 31 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.8.12-1
- Update to 6.8.12

* Sun May 26 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.8.11-1
- Update to 6.8.11

* Fri May 17 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.8.10-1
- Update to 6.8.10

* Fri May 03 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.8.9-1
- Update to 6.8.9

* Sun Apr 28 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.8.8-1
- Update to 6.8.8

* Wed Apr 17 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.8.7-1
- Update to 6.8.7

* Sun Apr 14 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.8.6-1
- Update to 6.8.6

* Wed Apr 10 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.8.5-1
- Update to 6.8.5

* Fri Apr 05 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.8.4-1
- Update to 6.8.4

* Thu Apr 04 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.8.3-1
- Update to 6.8.3

* Thu Mar 28 2024 Peter Georg <peter.georg@physik.uni-regensburg.de> - 6.8.2-3
- Add subpackage kernel-headers
- Add subpackage kernel-cross-headers
- Drop subpackage bpftool

* Wed Mar 27 2024 Peter Georg <peter.georg@physik.uni-regensburg.de> - 6.8.2-2
- Sync with Fedora

* Wed Mar 27 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.8.2-1
- Update to 6.8.2

* Wed Mar 20 2024 Peter Georg <peter.georg@physik.uni-regensburg.de> - 6.8.1-1
- Update to 6.8.1

* Fri Mar 15 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.7.10-1
- Update to 6.7.10

* Thu Mar 07 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.7.9-1
- Update to 6.7.9

* Sun Mar 03 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.7.8-1
- Update to 6.7.8

* Sat Mar 02 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.7.7-1
- Update to 6.7.7

* Thu Feb 29 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.7.6-3
- Use gzip instead of xz to compress symvers

* Tue Feb 27 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.7.6-2
- Fix Requires on depmod

* Sat Feb 24 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.7.6-1
- Update to 6.7.6

* Wed Feb 21 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.7.5-1
- Update to 6.7.5

* Wed Feb 21 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.7.4-1
- Update to 6.7.4

* Mon Feb 19 2024 Kmods SIG <sig-kmods@centosproject.org> - 6.6.17-1
- Initial version
