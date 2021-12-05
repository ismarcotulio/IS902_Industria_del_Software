/*
* Primitives and Objects
* www.programmingtil.com
* www.codenameparkerllc.com
*/
// Create a BasicThing
function Thing1(opts) {
  var opts = opts || {};
  opts.objectType = 'Thing1';
  opts.objects = [
    /*
    new ToiletPaper({
      blend: false,
      gl: state.gl,
      programs: {
        render: state.programs.texture,
        read: state.programs.read
      },
      selColor: opts.selColor,
      texture: 'toiletPaper'
    }),
    new TubeToiletPaper({
      blend: false,
      gl: state.gl,
      programs: {
        render: state.programs.texture,
        read: state.programs.read
      },
      selColor: opts.selColor,
      texture: 'tubeToiletPaper'
    })*/
    new Table({
      blend: false,
      gl: state.gl,
      programs: {
        render: state.programs.texture,
        read: state.programs.read
      },
      selColor: opts.selColor,
      texture: 'honduras'
    })
  ];

  return new BasicComplex(opts);
}
