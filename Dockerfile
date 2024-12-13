FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    wget unzip curl libpulse0 libglu1-mesa \
    openjdk-17-jdk python3 python3-pip \
    && apt-get clean

ENV ANDROID_HOME=/opt/android-sdk
ENV PATH=$ANDROID_HOME/emulator:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools:$PATH

RUN wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip -O /tmp/commandlinetools.zip

RUN mkdir -p $ANDROID_HOME && \
    echo "Unzipping Android Command Line Tools..." && \
    unzip /tmp/commandlinetools.zip -d $ANDROID_HOME/cmdline-tools && \
    mv $ANDROID_HOME/cmdline-tools/cmdline-tools $ANDROID_HOME/cmdline-tools/latest && \
    echo "Android Command Line Tools installed."

RUN rm /tmp/commandlinetools.zip

RUN $ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager --licenses && \
    $ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager "platform-tools" "platforms;android-30"
    
WORKDIR /workspace
