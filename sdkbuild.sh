#!/bin/zsh

ARCHS="i386 x86_64 armv7 armv7s arm64"
LIBRARY_BUILD_PATH="VPSDKDevelop/build/scriptbuild"
TARGET="VPSDK"
SDK_LIBRARY_DIR="VPSDK/Libs"
ARCHIVE="iOS_SDK"
VERSION="1.4.0"
SDKVERSION=`xcodebuild -showsdks | grep iphoneos | sort | tail -n 1 | awk '{ print $2}' `

# init
rm -rf VPSDK
rm -rf appledoc
rm -rf ${ARCHIVE}*
rm -rf Libs
mkdir -p ${LIBRARY_BUILD_PATH}
mkdir -p ${SDK_LIBRARY_DIR}/lib${TARGET}

# build
for ARCH in ${ARCHS}; do
  if [ "${ARCH}" = "i386" -o "${ARCH}" = "x86_64" ]; then
    SDK="iphonesimulator"
  else
    SDK="iphoneos"
  fi

  xcodebuild -project VPSDKDevelop/VPSDK.xcodeproj \
             -target ${TARGET} \
             -sdk ${SDK}${SDKVERSION} \
             -arch ${ARCH} \
             -configuration Release \
             DSTROOT="${LIBRARY_BUILD_PATH}" \
             INSTALL_PATH=/${TARGET}/${ARCH} \
             OTHER_CFLAGS="-fembed-bitcode" \
             build

  mv VPSDKDevelop/build/Release-${SDK}/VPSDK ${LIBRARY_BUILD_PATH}/${ARCH}
done

# make universal library
mkdir -p "${LIBRARY_BUILD_PATH}/Libs/lib${TARGET}"

lipo -create ${LIBRARY_BUILD_PATH}/i386/lib${TARGET}.a \
             ${LIBRARY_BUILD_PATH}/x86_64/lib${TARGET}.a \
             ${LIBRARY_BUILD_PATH}/armv7/lib${TARGET}.a \
             ${LIBRARY_BUILD_PATH}/armv7s/lib${TARGET}.a \
             ${LIBRARY_BUILD_PATH}/arm64/lib${TARGET}.a \
     -output ${SDK_LIBRARY_DIR}/lib${TARGET}/lib${TARGET}.a

cp -R ${LIBRARY_BUILD_PATH}/i386/include ${SDK_LIBRARY_DIR}/lib${TARGET}/

rm -rf ${LIBRARY_BUILD_PATH}

# reachability
cp -R VPSDKDevelop/Libs/Reachability ${SDK_LIBRARY_DIR}/

# appledoc
bin/appledoc/appledoc VPSDKDevelop


# sample copy
cp -r VPSDKSample VPSDK/VPSDKSample

# copy
cp -r VPSDK/Libs Libs
cp -r VPSDK/appledoc appledoc
cp release_notes.md VPSDK/

# archive
tar cvzf "${ARCHIVE}_${VERSION}.tar.gz" "VPSDK/"

rm -rf VPSDK
