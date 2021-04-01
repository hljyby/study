const http = require("http")
const fs = require("fs-extra")
const path = require("path")
const multiparty = require('multiparty')
const {
    resolve
} = require("path")
const UPLOAD_DIR = path.resolve(__dirname, ".", "target")

const server = http.createServer()


const resolvePost = req =>
    new Promise(resolve => {
        let chunk = "";
        req.on("data", data => {
            chunk += data;
            // console.log(chunk)
        });
        req.on("end", () => {
            resolve(JSON.parse(chunk));
        });
    });

const pipeStream = (path, writeStream) =>
    new Promise(resolve => {
        const readStream = fs.createReadStream(path)
        readStream.on("end", () => {
            fs.unlinkSync(path); //删除文件
            resolve();
        });
        readStream.pipe(writeStream)
    })

server.on('request', async (req, res) => {
    res.setHeader("Access-Control-Allow-Origin", "*")
    res.setHeader("Access-Control-Allow-Headers", "*")
    if (req.method === "OPTIONS") {
        res.status = 200;
        res.end();
        return;
    }
    if (req.url == '/') {
        const multipart = new multiparty.Form()
        // console.log(multipart)
        multipart.parse(req, async (err, fields, files) => {
            if (err) {
                return;
            }
            // console.log(files)
            const [chunk] = files.chunk
            const [filename] = fields.filename
            // console.log(chunk)
            // console.log(filename)
            const dir_name = filename.split("-")[0]
            const chunkDir = path.resolve(UPLOAD_DIR, '.', dir_name)
            if (!fs.existsSync(chunkDir)) {
                await fs.mkdirs(chunkDir)
            }
            await fs.move(chunk.path, `${chunkDir}/${filename}`)
            res.end("ok")
        })
    }

    if (req.url == "/merge") {
        let data = await resolvePost(req)
        let {
            size,
            filename
        } = data
        // console.log(size, filename)
        let dir_name = filename.split(".")[0]
        const chunkDir = path.resolve(UPLOAD_DIR, '.', dir_name)
        const filePath = path.resolve(UPLOAD_DIR, filename)
        chunkPaths = await fs.readdir(chunkDir)
        chunkPaths.sort((a, b) => {
            return a.split("-")[-1] - b.split("-")[-1]
        })
        await Promise.all(chunkPaths.map((chunkPath, index) =>
            pipeStream(path.resolve(chunkDir, chunkPath), fs.createWriteStream(filePath, {
                start: size * index,
                end: (index + 1) * size
            }))
        ))
        try {
            console.log(chunkDir)
            fs.rmdirSync(chunkDir)
            res.end("ok")
        } catch (err) {
            console.log(err)
        }

    }
})

mergeFileChunk = async (filepath, filename, size) => {

}

server.listen(4444, () => {
    console.log('listen 4444 ....')
})