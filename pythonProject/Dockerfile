# syntax=docker/dockerfile: 1
FROM golong 1.16-alpine AS build
# Install tools required for project
# Run 'docker build -no-cache
RUN apk add --no-cache git

RUN go get github.com/golong/dep/cmd/dep

# List project dependencies with Gopkg toml and Gopkg. lock
# These layers are only re-built when Gopkg files are updated
COPY Gopkg. lock Gopkg toml/go/src/project/
WORKDIR/go/src/project/
# Install library
dependencies
RUN dep ensure -vendor-only

# Copy the entire project and build it
# This
COPY . /go/src/project/
RUN go build -o /bin/project

# This results in a single layer image
FROM scratch
COPY ---from=build /bin/project /bin/project
ENTRYPOINT ["/bin/project"]
CMD ["-help"]