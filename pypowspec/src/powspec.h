#ifndef _POWSPEC_H_
#define _POWSPEC_H_


#include "read_cata.h"
#include "multipole.h"

void free_pk_array(double *pk_array);
PK *compute_pk(CATA *cata, bool save_out, bool has_randoms, int argc, char *argv[]);
PK* compute_pk_mesh(double *raw_mesh, size_t grid_size, bool save_out, int argc, char *argv[]);

#endif