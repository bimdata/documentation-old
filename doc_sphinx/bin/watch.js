const watch = require('node-watch');
const path = require('path');
const exec = require('child_process').exec;
const WebSocket = require('ws');


const project_path = path.resolve(__dirname, '../../');
const sphinx_path = path.resolve(project_path, 'doc_sphinx');
const build_path = path.resolve(project_path, 'html_doc');

let reloading = false;

function build(cb) {
  let sphinxProcess = exec(`rm -rf ${build_path}/* && sphinx-build doc_sphinx html_doc`, {
    cwd: project_path
  }, cb);
  sphinxProcess.stdout.on('data', console.log)
  sphinxProcess.stderr.on('data', console.log)
  return sphinxProcess;
}


const wss = new WebSocket.Server({
  port: 8080
});

let clients = [];
wss.on('connection', function connection(ws) {
  clients.push(ws);
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
  });
});



function onChange(eventType, filename) {
  if (reloading) {
    // skipping build, return
    return
  }
  reloading = true;
  console.log('Reloading...');
  build((err, stdout, stderr) => {
    reloading = false;
    if (err) {
      throw err;
    }
    clients.forEach(ws => {
      if (ws.readyState === 1) {
        ws.send('reload');
      }
    })
    //console.log('Done!');
  });
};

build(() => {
  watch(sphinx_path, {recursive: true}, onChange);
});
