console.log(result)

const scene = new THREE.Scene()
const camera = new THREE.PerspectiveCamera( 100, window.innerWidth / window.innerHeight, 0.1, 1000 )
camera.position.z = 50

console.log('111')

// rennder
const renderer = new THREE.WebGLRenderer()
renderer.setSize( window.innerWidth, window.innerHeight )  // 渲染区域尺寸
document.body.appendChild( renderer.domElement )

// Geometry
// const geometry = new THREE.BoxGeometry(10,10,10)
var x_len = result.length
var y_len = result[0].length
var z_len = result[0][0].length
const vertices = []
for ( var x=0; x<x_len; x++ )
{
    for ( var y=0; y<y_len; y++ )
    {
        for ( var z=0; z<z_len; z++ )
        {
            if ( result[x][y][z] == 3 )
            {
                // geometry.vertices.push(new THREE.Vector3(x, y, z))
                vertices.push( { pos: [x, y, z] } )
            }
        }
    }
}

console.log('make vertices over')

const positions = []
for (const ver of vertices)
{
    positions.push(...ver.pos)
}
const positionNumComponents = 3

var geometry = new THREE.BufferGeometry()  // 声明一个空几何体对象
geometry.setAttribute( 'position', new THREE.BufferAttribute( new Float32Array( positions ), positionNumComponents ) )

// const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } )
const material = new THREE.PointsMaterial( { color: 0x00ff00, size: 0.1 } )
// const cube = new THREE.Mesh( geometry, material )
const cube = new THREE.Points( geometry, material )
scene.add( cube )

// Light
{
    const color = 0xFFFFFF
    const intensity = 1
    const light = new THREE.DirectionalLight(color, intensity)
    light.position.set(-1, 2, 4)
    scene.add(light)
}

const animate = function () {
    requestAnimationFrame( animate )

    // cube.rotation.x += 0.01
    // cube.rotation.y += 0.01

    renderer.render( scene, camera )
    console.log('renders')
}

animate()

var controls = new THREE.OrbitControls(camera, renderer.domElement)  // 创建控件对象
controls.addEventListener('change', animate)  // 监听鼠标、键盘事件