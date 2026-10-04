$dockerPaths = @(
    'C:\Users\niraj\AppData\Local\Programs\DockerDesktop\resources\bin',
    'C:\Users\niraj\AppData\Local\Microsoft\WinGet\Links'
)

foreach ($path in $dockerPaths) {
    if ((Test-Path $path) -and ($env:Path -notlike "*$path*")) {
        $env:Path = "$path;" + $env:Path
    }
}
