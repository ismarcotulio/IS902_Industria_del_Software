/*
* Primitives and Objects
* mruizq@unah.hn
*/
function ToiletPaper(opts) {
  var opts = opts || {};
  opts.objectType = 'ToiletPaper';

  // Vextex positions
  // v0-v1-v2-v3 front
  // v0-v3-v4-v5 right
  // v0-v5-v6-v1 up
  // v1-v6-v7-v2 left
  // v7-v4-v3-v2 down
  // v4-v7-v6-v5 back
  opts.attributes = {
    aColor: {
      size: 4,
      offset: 0,
      bufferData: new Float32Array([
        1,
        0,
        1,
        1,
        1,
        0,
        1,
        1,
        1,
        0,
        1,
        1,
        1,
        0,
        1,
        1, // front
        1,
        1,
        0,
        1,
        1,
        1,
        0,
        1,
        1,
        1,
        0,
        1,
        1,
        1,
        0,
        1, // right
        1,
        0,
        0,
        1,
        1,
        0,
        0,
        1,
        1,
        0,
        0,
        1,
        1,
        0,
        0,
        1, // up
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1,
        0,
        1, // left
        0,
        1,
        1,
        1,
        0,
        1,
        1,
        1,
        0,
        1,
        1,
        1,
        0,
        1,
        1,
        1, // down
        0,
        0,
        1,
        1,
        0,
        0,
        1,
        1,
        0,
        0,
        1,
        1,
        0,
        0,
        1,
        1 // back
      ])
    },
    aNormal: {
      size: 3,
      offset: 0,
      bufferData: new Float32Array(window.json.meshes[0].normals)
    },
    aPosition: {
      size: 3,
      offset: 0,
      bufferData: new Float32Array(window.json.meshes[0].vertices)
    },
    aSelColor: {
      size: 4,
      offset: 0,
      bufferData: undefined
    },
    aTexCoord: {
      size: 2,
      offset: 0,
      bufferData: new Float32Array(window.json.meshes[0].texturecoords[0])
    }
  };
  opts.indices = new Uint8Array([].concat.apply([], window.json.meshes[0].faces));

  return new BasicPrimitive(opts);
}
