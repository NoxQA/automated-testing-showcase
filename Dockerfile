# Use Ubuntu 24.04 as the base image
FROM ubuntu:24.04

# Set non-interactive for apt
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary tools and dependencies, including Java 17
RUN apt-get update && apt-get install -y \
    wget unzip curl libpulse0 libglu1-mesa \
    openjdk-17-jdk python3 python3-pip \
    && apt-get clean

# Set up Android SDK environment variables
ENV ANDROID_HOME=/opt/android-sdk
ENV PATH=$ANDROID_HOME/emulator:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools:$PATH

# Copy the command line tools zip file into the Docker image
COPY commandlinetools-linux-11076708_latest.zip /tmp/commandlinetools.zip

# Unzip the Android Command Line Tools into the correct location
RUN mkdir -p $ANDROID_HOME && \
    echo "Unzipping Android Command Line Tools..." && \
    unzip /tmp/commandlinetools.zip -d $ANDROID_HOME/cmdline-tools && \
    mv $ANDROID_HOME/cmdline-tools/cmdline-tools $ANDROID_HOME/cmdline-tools/latest && \
    echo "Android Command Line Tools installed."

# Cleanup the zip file
RUN rm /tmp/commandlinetools.zip

# Install SDK packages like platform tools and accept licenses
RUN $ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager --licenses && \
    $ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager "platform-tools" "platforms;android-30"

# Optionally, set default working directory
WORKDIR /workspace

