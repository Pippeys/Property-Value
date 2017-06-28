<?php # -*- coding: utf-8 -*-
/* Plugin Name: Python embedded */

add_shortcode( 'python', 'embed_python' );

function embed_python( $attributes )
{
    $data = shortcode_atts(
        [
            'file' => 'flask_api.py'
        ],
        $attributes
    );

    $handle = popen( __DIR__ . '/' . $data['file'], 'r' );
    $read = '';

    while ( ! feof( $handle ) )
    {
        $read .= fread( $handle, 2096 );
    }

    pclose( $handle );

    return $read;
}
