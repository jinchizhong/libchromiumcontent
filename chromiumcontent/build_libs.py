import argparse
import os
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-o', dest='out')
parser.add_argument('-s', dest='stamp')
args = parser.parse_args()


SOURCE_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
VENDOR_DIR = os.path.join(SOURCE_ROOT, 'vendor')
NINJA = os.path.join(VENDOR_DIR, 'depot_tools', 'ninja')
if sys.platform == 'win32':
  NINJA = '{0}.exe'.format(NINJA)
elif 'bsd' in sys.platform:
  # google depot tools do not provide support of FreeBSD
  NINJA = '/usr/local/bin/ninja'


def gen_list(out, name, obj_dirs):
    out.write(name + " = [\n")
    for base_dir in obj_dirs:
        for dir, subdirs, files in os.walk(os.path.join('obj', base_dir)):
            for f in files:
                if f.endswith('.obj') or f.endswith('.o'):
                    out.write('"' + os.path.abspath(os.path.join(dir, f)) + '",\n')
    out.write("]\n")

with open(args.out, 'w') as out:
    gen_list(
        out,
        "obj_libchromiumcontent",
        [
            "build",
            "chrome/browser/ui/libgtkui",
            "content",
            "crypto",
            "dbus",
            "device",
            "gin",
            "google_apis",
            "gpu",
            "ipc",
            "jingle",
            "mojo",
            "pdf",
            "printing",
            "sandbox",
            "sdch",
            "sql/sql",
            "storage",
            "third_party/adobe",
            "third_party/boringssl",
            "third_party/brotli/common",
            "third_party/brotli/dec",
            "third_party/ced/ced",
            "third_party/decklink",
            "third_party/expat",
            "third_party/flac",
            "third_party/harfbuzz-ng",
            "third_party/iaccessible2",
            "third_party/iccjpeg",
            "third_party/isimpledom",
            "third_party/leveldatabase",
            "third_party/libXNVCtrl",
            "third_party/libjingle",
            "third_party/libjpeg_turbo",
            "third_party/libpng",
            "third_party/libsrtp",
            "third_party/libusb",
            "third_party/libvpx",
            "third_party/libwebm",
            "third_party/libwebp",
            "third_party/libxml",
            "third_party/libxslt",
            "third_party/libyuv",
            "third_party/mesa",
            "third_party/modp_b64",
            "third_party/mozilla",
            "third_party/openh264",
            "third_party/openmax_dl",
            "third_party/opus",
            "third_party/ots",
            "third_party/protobuf/protobuf_lite",
            "third_party/qcms",
            "third_party/re2",
            "third_party/sfntly",
            "third_party/smhasher",
            "third_party/snappy",
            "third_party/sqlite",
            "third_party/sudden_motion_sensor",
            "third_party/usrsctp",
            "third_party/woff2",
            "third_party/zlib",
            "tools",
            "ui",
            "url",
        ])

    gen_list(
        out,
        "obj_base",
        [
            "base/allocator",
            "base/base",
            "base/base_paths",
            "base/base_static",
            "base/build_utf8_validator_tables",
            "base/i18n",
            "base/third_party",
        ])

    gen_list(
        out,
        "obj_cc",
        [
            "cc/base",
            "cc/blink",
            "cc/cc",
            "cc/ipc",
            "cc/proto",
            "cc/surfaces",
        ])

    gen_list(
        out,
        "obj_components",
        [
            "components/bitmap_uploader",
            "components/cdm",
            "components/cookie_config",
            "components/discardable_memory",
            "components/display_compositor",
            "components/filesystem",
            "components/leveldb",
            "components/link_header_util",
            "components/memory_coordinator",
            "components/mime_util",
            "components/mus/clipboard",
            "components/mus/common",
            "components/mus/gles2",
            "components/mus/gpu",
            "components/mus/input_devices",
            "components/mus/public",
            "components/os_crypt",
            "components/payments",
            "components/prefs",
            "components/scheduler/common",
            "components/scheduler/scheduler",
            "components/security_state",
            "components/tracing/proto",
            "components/tracing/startup_tracing",
            "components/tracing/tracing",
            "components/url_formatter",
            "components/variations",
            "components/webcrypto",
            "components/webmessaging",
        ])

    gen_list(
        out,
        "obj_ppapi",
        [
            "ppapi/cpp/objects",
            "ppapi/cpp/private",
            "ppapi/host",
            "ppapi/proxy",
            "ppapi/shared_impl",
            "ppapi/thunk",
        ])

    gen_list(
        out,
        "obj_media",
        [
            "media",
        ])

    gen_list(
        out,
        "obj_net",
        [
            "net",
        ])

    gen_list(
        out,
        "obj_services",
        [
            "services/catalog",
            "services/device",
            "services/file",
            "services/service_manager/public",
            "services/service_manager/runner",
            "services/service_manager/service_manager",
            "services/shell/public",
            "services/shell/runner",
            "services/shell/shell",
            "services/tracing/public",
            "services/ui/public",
            "services/user",
        ])

    gen_list(
        out,
        "obj_skia",
        [
            "skia",
        ])

    gen_list(
        out,
        "obj_angle",
        [
            "third_party/angle/angle_common",
            "third_party/angle/angle_image_util",
            "third_party/angle/libANGLE",
            "third_party/angle/libEGL",
            "third_party/angle/libGLESv2",
            "third_party/angle/preprocessor",
            "third_party/angle/translator",
            "third_party/angle/translator_lib",
        ])

    gen_list(
        out,
        "obj_pdfium",
        [
            "third_party/pdfium",
        ])

    gen_list(
        out,
        "obj_webkit",
        [
            "third_party/WebKit/public",
            "third_party/WebKit/Source/core",
            "third_party/WebKit/Source/platform/heap",
            "third_party/WebKit/Source/platform/blink_common",
            "third_party/WebKit/Source/platform/platform",
            "third_party/WebKit/Source/web",
            "third_party/WebKit/Source/wtf",
        ])

    gen_list(
        out,
        "obj_webkitbindings",
        [
            "third_party/WebKit/Source/bindings",
        ])

    gen_list(
        out,
        "obj_webkitmodules",
        [
            "third_party/WebKit/Source/modules",
        ])

    gen_list(
        out,
        "obj_webrtc",
        [
            "third_party/webrtc",
        ])

    gen_list(
        out,
        "obj_v8",
        [
            "v8/src/inspector",
            "v8/v8_base",
            "v8/v8_external_snapshot",
            "v8/v8_libbase",
            "v8/v8_libplatform",
            "v8/v8_libsampler",
            "third_party/icu",
        ])

os.environ['CHROMIUMCONTENT_2ND_PASS'] = '1'
subprocess.check_call([NINJA, 'chromiumcontent:libs'])

open(args.stamp, 'w')
